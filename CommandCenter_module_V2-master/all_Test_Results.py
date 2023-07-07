"""
Ce fichier crée un rapport des tests réussis sur tous les
fichiers de test du dossier actuel et indique le pourcentage
de tests passés et échoués.
"""

import unittest
import os

directory = '/home/pi/.virtualenvs/CommandCenter/'
tester = unittest.defaultTestLoader.discover(directory)
run = unittest.TextTestRunner()
result = run.run(tester)
passed = result.testsRun - len(result.failures) - len(result.errors)
percentage = passed / result.testsRun * 100
print(f'{percentage}% of test cases passed.')