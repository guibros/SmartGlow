"""
Ce fichier crée est le fichier principal du centre de commande.
Il reçoit des messages MQTT concernant l'état de l'identification
faciale et traite les informations pour afficher les informations
appropriées sur l'interface graphique et lire l'audio approprié.
Ce fichier contient la boucle centrale principale pour l'ensemble
du programme et gère tous les changements d'état.
"""

from mqttConfig import MQTTcontroller
from datetime import datetime as dt
from atlasProfilv2 import RPA
from threading import Thread
from meteo import Weather
from NLPclass import NLP
from enum import Enum
import display
import time
from log_Monitor import Monitor


# Set up log-monitor for troubleshooting
monitor = Monitor()
logger = monitor.logger('log_CommandCenter')


# Instantiation of Database, Natural Language Processing and Weather module
RPA_db = RPA()  # Database
nlp = NLP()  # NLP
weather = Weather()  # Weather

# Setting default MQTT Message and user for tests
DEFAULTMQTTMESSAGE = 'Nothing' # <--Use this when NOT TESTING
# DEFAULTMQTTMESSAGE = 'Identified: ' # <--Use this WHEN TESTING  (Also change "# Get UserId" for tests)

# Set a default user
DEFAULTUSER = 'Phil'

# Creating STATE state machine class
class STATE(Enum):
    baseState = "basestate"
    objectState = "objectState"
    identificationDelay = 'identificationDelay'
    unknownState = 'unknownstate'
    facialState = "facialstate"

# Creating SCENE state machine class
class Scene(Enum):
    none = "none"
    positive = "positive"
    negative = "negative"

# Creating main CommandCenter class 
class CommandCenter:
    def __init__(self):
        self.MQTTState = MQTTcontroller(default=DEFAULTMQTTMESSAGE)
        self.MQTTState.subscription('AHUNTSIC-PROJ-INT/identity')
        self.sentimentCheck = True
        self.CurrentSTATE = STATE.baseState
        self.SceneSTATE = Scene.none
        self.running = True
        self.CurrentUSER = None
        
        # # User occupied hook
        # self.BUSY_WITH_USER = True
        
        # GUI variables
        self.main = ''
        self.spinner = ''
        self.secondary = ''
        

    # This method starts the gTTS in a thread to allow quicker loading of the listening
    def speakQuick(self, text):
        speechThread = Thread(target=nlp.speak, args=(text, ))
        speechThread.start()


    # Speech grabbing for x amount of tries before ending
    def grabSpeechData(self, tryCount):
        data = ""
        counter = 0
        while data == "" and counter != tryCount:
            if counter != 0:
                logger.debug('Ask to repeat')
                self.speakQuick("Pouvez-vous s'il vous plait répéter?")
            time.sleep(1)
            data = nlp.listen()
            counter += 1
        if data == "":
            logger.debug('SPEACH FAILURE..No audible response')
            raise Exception('No audible response')
        logger.debug(f"User's response: {data}")
        return data

     
    # This method restarts or ends an interaction loop after a complete interaction cycle 
    def needMoreAssistance(self):
        display.otherRequest(self)
        self.speakQuick("Avez-vous besoin d'autres chose?")
        try:
            data = self.grabSpeechData(3)
            if nlp.analyzeVariable(data, 'oui'):
                return True
            else:
                return False 
        except:
            nlp.speak("Je n'ais pas pu saisir votre réponse. Je termine donc cette scéance.")
            return False


    # This method sets ending states and variables
    def endInteraction(self):
        display.turnOff(self)
        nlp.speak('Au revoir.')
        time.sleep(5)
        self.CurrentSTATE = STATE.baseState
        self.SceneSTATE = Scene.none
        self.sentimentCheck = True
        display.showNothing(self)  
        time.sleep(10)
        return False

    # Get user from database
    def getCurrentUSER(self):
        # Get UserId 
        UserID = self.MQTTState.message  # <-- Use this when NOT TESTING
        # UserID = DEFAULTUSER  # <-- Use this WHEN TESTING
        logger.debug(f"UserID: {UserID}")
        
        # Save user info
        userInfo = RPA_db.findClient(UserID)
         
        # Failsafe if DB Returns None
        if userInfo == None:
            logger.debug("*Used DEFAULT user")
            return RPA_db.findClient(DEFAULTUSER)  # Put a default user
        
        logger.debug(f'UserINfo: {userInfo}')
        return userInfo

    # This is the main loop thread
    def runCommandCenter(self):
        
        # PRIMARY LOOP
        while self.running:

            logger.debug("MAIN LOOP RUNNING NEW")
            logger.debug(f"MQTT MESSAGE CHECK: {self.MQTTState.message}")
            
            # lecture des signaux MQTT et ajustement de MQTTState
            if self.MQTTState.message == 'Nothing':  # State settting when nothing in proximity
                self.CurrentSTATE = STATE.baseState
            elif self.MQTTState.message == 'Object':  # State settting when object in proximity
                self.CurrentSTATE = STATE.baseState
            elif self.MQTTState.message == 'IdentificationDelay':  # State settting when face in proximity
                self.CurrentSTATE = STATE.identificationDelay
            elif self.MQTTState.message == 'Unknown':  # State settting when unknonw face  in proximity
                self.CurrentSTATE = STATE.unknownState 
            elif self.MQTTState.message != None:  # State settting when recognized face  in proximity
                self.CurrentSTATE = STATE.facialState
            
            logger.debug(f"Current state: {self.CurrentSTATE}")  # Check setting of state
            
                            
            # Main STATE MACHINE
            if self.CurrentSTATE == STATE.baseState:
                display.showNothing(self)
                self.sentimentCheck = True
            elif self.CurrentSTATE == STATE.identificationDelay:
                display.identificationProcess(self)
            elif self.CurrentSTATE == STATE.unknownState:
                display.unknownUser(self)
            elif self.CurrentSTATE == STATE.facialState:  # If the face is recognized
                
                # Lock below code below with identified user 
                self.CurrentUSER = self.getCurrentUSER()
                
                if self.CurrentUSER['ClientInfo']['firstName'] == 'DEFAULT':
                    logger.debug('Default user activated')
                    display.defaultUser(self)
                    nlp.speak('Usager non retrouvé dans la base de données')
                    self.endInteraction()
                    continue  # Break out of the main CommandCenter loop and start again
                    
                
                # Get the users name 
                userName = self.CurrentUSER['ClientInfo']['firstName']
                logger.debug(f"Current users user name: {userName}")
                display.identifiedUser(self, userName)
                
                # If sentimentCheck variable True, do sentiment analysis
                if self.sentimentCheck:
                    self.speakQuick(f"Bonjour {userName}, Comment vous sentez-vous?")
                    try:
                        data = self.grabSpeechData(3)
                    except:
                        self.endInteraction()
                        continue  # Break out of the main CommandCenter loop and start again
                    
                    # Analyze response sentiment
                    SentimentState = nlp.sentimentAnalisys(data)
                    if SentimentState == "POS":
                        self.SceneSTATE = Scene.positive
                        print(Scene.positive)
                    elif SentimentState == "NEU" or SentimentState == "NEG":
                        self.SceneSTATE = Scene.negative   
                        print(Scene.negative)
                    self.sentimentCheck = False
                
            
            #######################
            # SECTION SCENE STATE #
            #######################
            
            if self.SceneSTATE == Scene.positive:
                
                # SECONDARY LOOP:
                while self.MQTTState.message != 'Nothing':
                    
                    display.positiveMenu(self, userName)
                    self.speakQuick(f'Comment puis-je vous aider {userName}?')
                    try:
                        data = self.grabSpeechData(3)
                    except:
                        nlp.speak("Je n'ais pas pu saisir votre réponse. Je termine donc cette scéance.")
                        self.endInteraction()
                        break  # Break out of SECONDARY LOOP and go back to main loop
                    
                    # Set userRequest variable
                    userRequest = nlp.analyze(data)
                    logger.debug(f"User request subject: {userRequest}")
                    
                    # Handle user's request
                    if userRequest == 'heure':
                        display.time(self)
                        response = f"Il est présentement {dt.now().strftime('%I:%M')}"
                        nlp.speak(response)
                    elif userRequest == 'meteo':
                        display.meteo(self, weather.currentWeather()[1])
                        nlp.speak(weather.currentWeather()[0])
                    elif userRequest == 'meteo futur':
                        display.meteoFuture(self, weather.currentForecast()[1])
                        nlp.speak(weather.currentForecast()[0])
                    elif userRequest == 'medicament':
                        medList = [(x['Name'], x['Dosage']) for x in self.CurrentUSER['Medication'].values()]
                        medNames = [med[0] for med in medList]
                        display.medication(self, '\n'.join(medNames))
                        nlp.speak(f"Vous prenez les médicaments suivants: {medList}.")
                    elif userRequest == 'meeting':
                        appointments = [(x['Name'], x['Date'], x['Time'], x['Location']) for x in self.CurrentUSER['Appointments'].values()]
                        days = [app[1].split(',')[1] for app in appointments]
                        apptms = [f"{app[0]},    {app[1]},    {app[2]}" for app in appointments]
                        display.appointments(self, '\n'.join(apptms))
                        nlp.speak(f"Vous avez des rendez-vous le: {days[0]}, {days[1]} et le {days[2]}")
                    elif userRequest == 'medecin':
                        medContacts = [(x['Name'], x['Last'], x['Telephone']) for x in self.CurrentUSER['Contacts'].values() if x['Type'] == 'médical']
                        docNames = [f"{x[0]} {x[1]}" for x in medContacts]
                        display.medicalContacts(self,  '\n'.join(docNames))
                        nlp.speak(f"Vos médecins sont: {docNames}")
                    elif userRequest == 'contact':
                        types = set((x['Type'].capitalize()) for x in self.CurrentUSER['Contacts'].values())
                        display.typeOfContacts(self,  '\n'.join(types))
                        self.speakQuick(f"Voici vos listes de contacts. Laquelle voulez-vous consulter?")
                        time.sleep(3)
                        try:
                            listResponse = self.grabSpeechData(3)
                            for type in types:
                                print(f"********** the response: {listResponse}, the type: {type}")
                                if nlp.analyzeVariable(listResponse.lower(), type.lower()):
                                    nameListType = [(x['Name'], x['Last']) for x in self.CurrentUSER['Contacts'].values() if x['Type'] == type.lower()]
                                    print(f"Namelisttype: {nameListType}")
                                    nameList =  [f"{x[0]} {x[1]}" for x in nameListType]
                                    print(f"Namelist: {nameList}")
                                    display.contactsRequested(self,  '\n'.join(nameList))
                                    nlp.speak(f"Vos contact {type} sont: {nameList}")
                        except:
                            nlp.speak("Je n'ais pas pu saisir votre réponse. Je termine donc cette scéance.")
                            self.endInteraction()
                            break   
                    elif userRequest == 'activite':
                        activities = [(x['Name'], x['Date'], x['Time'], x['Location']) for x in self.CurrentUSER['Activity'].values()]
                        days = [act[1] for act in activities]
                        acts = [f"{act[0]} le {act[1]} à {act[2]}" for act in activities]
                        display.activities(self, '\n'.join(acts))
                        nlp.speak(f"Vos trois prochaines activitées sont: {acts}")           
                
                    # Check to see if proximity is still there and then Repeat or Exit
                    if self.MQTTState.message != 'Nothing' and self.needMoreAssistance():
                        continue
                    else:
                        self.endInteraction()
                        logger.debug("\n\n**** ENDING SESSION ****\n\n")
                        break
                
                else:  # If none of the above user requests is satisfied or if no proximity
                    self.endInteraction()
                    continue  # Break out of SECONDARY LOOP and go back to main loop

            elif self.SceneSTATE == Scene.negative:      
                self.speakQuick("Vous semblez en difficulté, nous vous suggerons de contacter une des personnes suivantes:")
                urgenceContactsList = [(x['Name'], x['Last'], x['Telephone']) for x in self.CurrentUSER['Contacts'].values() if x['Type'] == 'urgence']
                urgenceContactsNames = [f"{x[0]} {x[1]}" for x in urgenceContactsList]
                display.userAideMenu(self, '\n'.join(urgenceContactsNames))
                time.sleep(10)
                self.SceneSTATE = Scene.positive  # Go back to waiting for user's request
            
            # If user leaves the proximity, 'continue' out of the main loop and check proximity
            else:
                continue           
             
            # Close loop only for testing purposes
            # self.running = False
 
            time.sleep(0.5)
        logger.debug('Command Center Loop ending')

if __name__ == '__main__':
    try:
        # Instantiation of Database, Natural Language Processing and Weather module
        RPA_db = RPA()  # Database
        nlp = NLP()  # NLP
        weather = Weather()  # Weather
        
        # Run Command Center loop Thread
        cc = CommandCenter()
        commandCenterThread = Thread(target=cc.runCommandCenter)
        commandCenterThread.start()

    except KeyboardInterrupt:
        cc.running = False