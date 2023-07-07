"""
Ce fichier contient la classe qui gère tout le traitement
du langage naturel ainsi que le traitement et l'analyse de la voix.
"""


from gtts import gTTS
import os
import speech_recognition as speechRecognition
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer
import phrases_models as strings_


class NLP:
    def __init__(self):
        self.recognizer = speechRecognition.Recognizer()
        self.sia = SentimentIntensityAnalyzer()
        self.phrases = strings_.phrases
        
    def speak(self, text):
        tts = gTTS(text=text, lang='fr', tld='ca')
        audioFile = "audio.mp3"
        tts.save(audioFile)
        os.system('mpg321 audio.mp3')
        
    def listen(self):
        with speechRecognition.Microphone() as source:
            self.recognizer.pause_threshold = 1
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening to user response...")
            audioData = self.recognizer.listen(source, 5, 10) 
            try:
                data = self.recognizer.recognize_google(audioData, language="fr-FR")
                print(f"User response: {data}")
                return data
            except:
                print("Unable to grab user response.")
                return ""      
                
    def sentimentAnalisys(self, data):
        score = self.sia.polarity_scores(data)
        if score['compound'] >= 0.05:
            return "POS"
        elif score['compound'] > -0.05 and score['compound'] < 0.05:
            return "NEU"
        elif score['compound'] <= -0.05:
            return "NEG"

    def analyzeVariable(self, text, keyword):
        if keyword in text:
            return True
        else:
            return False

    def analyze(self, text):           
        if text == "":
            pass
        else:
            (modele, score) = process.extractOne(text, self.phrases)
            if score >= 89:
                for trigger, sampleModel in strings_.models_dict.items():
                    if modele in sampleModel:
                        return trigger
            else:
                print("Score < 90, analyzing with back-up Keyword method...")
                backupResponse = self.motClef(text)
                if backupResponse == None:
                    print("Command incomprise.")
                    self.speak("Commande incomprise.")
                else:
                    return backupResponse

    def motClef(self, text):
        for word, trigger in strings_.keyWordDict.items():
            if word in text:
                return trigger