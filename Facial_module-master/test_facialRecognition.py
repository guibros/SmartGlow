"""
Ce fichier est un fichier de test pour le fichier de reconnaissance faciale
"""

import unittest
from facial_recognition import Recognizer
import time

recognizer = Recognizer()

class TestFacialRecognition(unittest.TestCase):
    

    def test_forAtLeast_x_seconds(self):
        initialTime = time.time()
        time.sleep(3)
        # Test should return False (3secs IS NOT >= 10secs)
        result1 = recognizer.forAtLeast_x_seconds(10, initialTime)
        self.assertEqual(result1, False)
        # Test should return True (3secs IS >= 2secs)
        result2 = recognizer.forAtLeast_x_seconds(2, initialTime)
        self.assertEqual(result2, True)

if __name__ == '__main__':
    unittest.main()