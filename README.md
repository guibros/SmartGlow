# WellCheck Mirror
Prototype for a health-oriented smart mirror with AI and NLP

## Description
A one-way mirror with an integrated screen and facial recognition performing operations on voice commands, connected to assistance and information services.

Three Raspberry Pis connected through MQTT:
- One Raspberry Pi with a proximity sensor detecting activity in front of the device and activating/deactivating the system.
- One Raspberry Pi managing the facial recognition system with a live feed camera and the trained models.
- One Raspberry Pi connected to the behind-the-mirror monitor, a microphone, and a speaker, managing the GUI, listening to voice commands, responding audibly and visually, and fetching data from different databases.

User flow is programmed through voice-activated "scenes" with specific configurations for each scene.



<p align="center">
 <img src="https://github.com/guibros/WellCheckMirror/assets/116329812/52880d63-e1c4-4aee-8d10-4faac67776b9" alt="WellCheckMirror gif" width="33%">  <img src="https://github.com/guibros/WellCheckMirror/assets/116329812/36d8c9b7-9dc4-44e4-800a-a10ad14c15af" alt="WellCheckMirror gif 0" width="33%">  <img src="https://github.com/guibros/WellCheckMirror/assets/116329812/abc25ece-f084-4091-a12e-6b1bdbfe3fa1" alt="WellCheckMirror gif 1" width="33%"> 
</p>
<p align="center">
 <img src="https://github.com/guibros/WellCheckMirror/assets/116329812/8f4a3988-75a6-4d64-aae8-ca553818141a" alt="WellCheckMirror" width="25%">  <img src="https://github.com/guibros/WellCheckMirror/assets/116329812/d2e58b47-2507-4b9d-b175-5c7e3bf4b074" alt="WellCheckMirror (2)" width="25%">  <img src="https://github.com/guibros/WellCheckMirror/assets/116329812/906856c9-2035-449a-bbe3-34fd34185b58" alt="WellCheckMirror (1)" width="25%"> 
</p>


<br>
      
## Base Functions
- User detection
- Facial recognition
- Voice recognition
- Text-to-speech
- Graphical interface
- Wireless network connection
- MQTT network connection
- MongoDB database connection
- Sentiment analysis
- Time and date
- Current weather
- Weather forecasts
- Appointment schedule
- Activity schedules
- Address book consultation
- Consultation of the medical resources directory

## Hardware
- Microphone
- Speaker
- Screen
- Camera
- Proximity ultrasound sensor
- Three Raspberry Pis
- One-way mirror
- Custom-built MDF frame
- Switch

### Languages
Python

### Libraries/Modules
- _Artificial Intelligence_: Vader (sentiment analysis), Google Text To Speech (text-to-speech), SpeechRecognition (speech recognition), Fuzzywuzzy (intent classification), OpenCV (facial recognition)
- _IoT Communication_: Paho.MQTT (MQTT protocol)
- _Database_: PyMongo (MongoDB protocol)
- _Graphical User Interface_: Kivy (window display module)
- _Sensors_: RPi.GPIO (Raspberry Pi in/out board), Picamera (camera sensor for Raspberry Pi)

<br>
  
**This project was conceptualized, researched, programmed, and built in december 2022/january 2023 by Guillaume Brossard and Philip Louis.**
