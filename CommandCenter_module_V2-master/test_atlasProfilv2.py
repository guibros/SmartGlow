"""
Ce fichier est un fichier de test pour le fichier de base de données
"""

import unittest
from atlasProfilv2 import RPA

rpa = RPA()

class TestRPA(unittest.TestCase):
    
    def test_insertNewClient(self):
        rpa.insertNewClient('John', 'Test', 'Doe', '222-222-2222', '222 fake st., Montreal, Qubebec')
        successfulprofil = rpa.findClient('John')
        self.assertEqual(successfulprofil['ClientInfo']['Telephone'], '222-222-2222')
        self.assertEqual(successfulprofil['ClientInfo']['firstName'], 'Test')


if __name__ == '__main__':
    unittest.main()