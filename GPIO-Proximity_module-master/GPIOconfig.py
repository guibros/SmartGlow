"""
Ce fichier contrôle les broches GPIO pour le capteur de
proximité et il se connecte également à MQTT pour
envoyer des messages sur l'état de la proximité
"""

import RPi.GPIO as GPIO
from mqttConfig import MQTTcontroller
import time


class ProximitySensor:
    def __init__(self):
        self.TRIG = 11
        self.ECHO = 13
        self.distance = 0
        self.activated = True
        self.state = False
        self.THRESHOLD_DISTANCE = 120
        self.mqtt = MQTTcontroller()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def distanceCalc(self):
        GPIO.output(self.TRIG, 0)
        time.sleep(0.000002)

        GPIO.output(self.TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, 0)

        while GPIO.input(self.ECHO) == 0:
            a = 0
        time1 = time.time()
        while GPIO.input(self.ECHO) == 1:
            a = 1
        time2 = time.time()

        during = time2 - time1
        return during * 340 / 2 * 100

    def loop(self):
        while self.activated:
            self.distance = round(self.distanceCalc())
            if self.distance > self.THRESHOLD_DISTANCE and not self.state:
                self.state = True
                self.mqtt.publish('AHUNTSIC-PROJ-INT/proximity', f'basestate, noProximity, Distance: {self.distance}')
                print(f"Out of proximity: {self.distance}")
            if self.distance <= self.THRESHOLD_DISTANCE and self.state:
                self.state = False
                self.mqtt.publish('AHUNTSIC-PROJ-INT/proximity', f'proxistate, proximityDetected, Distance: {self.distance}')
                print(f"Within proximity: {self.distance}")
            time.sleep(2)
        return

    def destroy(self):
        print('\nProximity loop ended')
        GPIO.cleanup()



if __name__ == "__main__":
    proxi = ProximitySensor()
    proxi.setup()
    try:
        proxi.loop()
    except KeyboardInterrupt:
        proxi.activated = False
        proxi.destroy()