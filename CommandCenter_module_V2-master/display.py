"""
Ce fichier créé contient les fonctions nécessaires
pour afficher les bonnes informations sur l'interface graphique.
"""

from datetime import datetime as dt

def showNothing(display):
    display.main = ''
    display.secondary = ''
    display.spinner = 'images/black.png'

def identificationProcess(display):
    display.main = f''
    display.secondary = 'Identification en cours'
    display.spinner = 'images/wave.zip'
    
def unknownUser(display):
    display.main = 'Bienvenue chez'
    display.secondary = 'RPA Soleile\nwww.rpasoleile.org'

def identifiedUser(display, userName):
    display.main = f'Bonjour {userName}'
    display.secondary = "Comment vous sentez-vous?"
    display.spinner = 'images/speaking.zip'

def turnOff(display):
    display.main = 'Au Revoir'
    display.secondary = ''
    display.spinner = 'images/black.png'

def positiveMenu(display, userName):
    display.main = f'Comment puis-je vous aider {userName}?'
    display.secondary = "Dites une commande..."
    display.spinner = 'images/speaking.zip'

def time(display):
    display.main = "Il est présentement"
    display.secondary = dt.now().strftime('%I:%M')
    
def otherRequest(display):
    display.main = ''
    display.secondary = "Avez-vous besoin d'autres chose?"
    display.spinner = 'images/black.png'

def medication(display, medication):
    display.main = "Vos médicaments:"
    display.secondary = medication
    
def meteo(display, meteo):
    display.main = "La météo d'aujourd'hui:"
    display.secondary = meteo
    
def meteoFuture(display, meteoFuture):
    display.main = "Les prévisions météo:"
    display.secondary = meteoFuture

def appointments(display, appointments):
    display.main = "Vos rendez-vous:"
    display.secondary = appointments
    
def medicalContacts(display, doctors):
    display.main = "Vos medecins:"
    display.secondary = doctors
    
def typeOfContacts(display, types):
    display.main = "Vos listes de contacts:"
    display.secondary = types
    
def contactsRequested(display, contacts):
    display.main = "Vos contacts:"
    display.secondary = contacts

def activities(display, activities):
    display.main = "Vos activités:"
    display.secondary = activities

def userAideMenu(display, contacts):
    display.main = "Vos contacts d'urgence:"
    display.secondary = contacts
    display.spinner = 'images/speaking.zip'

def defaultUser(display):
    display.main = "Usager non retrouvé"
    display.secondary = 'dans la base données'
    display.spinner = 'images/black.png'