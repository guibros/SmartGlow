# CommandCenter Raspberry Pi

## Commandcenter.py:
Main program managing the mirror object, receiving MQTT commands, directing database queries, classifying received information, configuring scenes and steps based on configurations and commands received from MQTT or voice commands.

## GUI.py: 
Program controlling the Graphic User Interface, sending commands to the display window based on configurations and commands received from Commandcenter.py. Basic program for the GUI Raspberry Pi.
Display.py: Resource program for different graphical configurations.

## MQTTconfig.py:
Program controlling the MQTT broker's broadcast and listen protocols.

## Atlasprofil.py:
Program controlling data storage and retrieval from the database.

## NLPclass.py:
Program controlling various aspects of Natural Language Processing (text-to-speech, speech recognition, intent classification).

## METEO.py:
Program controlling the retrieval of weather-related data.