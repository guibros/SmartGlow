# WellCheck Mirror
Prototype for a health-oriented smart mirror with AI and NLP

## Description
A one-way mirror with an integrated screen and facial recognition performing operations on voice commands, connected to assistance and information services.

Three Raspberry Pis connected through MQTT:
- One Raspberry Pi with a proximity sensor detecting activity in front of the device and activating/deactivating the system.
- One Raspberry Pi managing the facial recognition system with a live feed camera and the trained models.
- One Raspberry Pi controlling the behind-the-mirror monitor, a microphone, and a speaker, managing the GUI, listening to voice commands, responding audibly and visually, and fetching data from different databases.

User flow is programmed through voice-activated "scenes" with specific configurations for each scene.

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

This project was conceptualized, researched, programmed, and built in december 2022/january 2023 by Guillaume Brossard and Philip Louis.
