"""
Ce fichier est un fichier de test pour le fichier MQTT
"""

import unittest
from mqttConfig import MQTTcontroller
import time



class TestMQTTcontroller(unittest.TestCase):
    
    # Check that MQTT is sending and receiving properly
    def test_runMQTT_send_receive(self):
        mqtt = MQTTcontroller()
        mqtt.subscription('AHUNTSIC/test')
        time.sleep(1)
        mqtt.publish('AHUNTSIC/test', 'This is a test')
        time.sleep(1)
        self.assertEqual(mqtt.message, 'This is a test')
        mqtt.stopMQTT

if __name__ == '__main__':
    unittest.main()