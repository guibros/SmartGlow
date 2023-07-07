"""
Ce fichier est un fichier de test pour le fichier de traitement de la voix
"""

import unittest
from NLPclass import NLP


nlp = NLP()

class TestNLPclass(unittest.TestCase):
    

    # Uncomment to test listen
    # def test_listen(self):
    #     # Say 'bonjour'
    #     self.assertEqual(nlp.listen(), 'bonjour')
    
    def test_sentimentAnalisys(self):
        self.assertEqual(nlp.sentimentAnalisys('Je suis heureux'), 'POS')
        self.assertEqual(nlp.sentimentAnalisys('Quelle est la météo'), 'NEU')
        self.assertEqual(nlp.sentimentAnalisys('Je suis triste'), 'NEG')

    def test_analyzeVariable(self):
        self.assertEqual(nlp.analyzeVariable('Contact ma famille', 'famille'), True)
        self.assertEqual(nlp.analyzeVariable('Contact ma famille', 'Famille'), False)      

    def test_analyze(self):
        self.assertEqual(nlp.analyze('quel heure est-il'), 'heure')
        self.assertEqual(nlp.analyze('quelle est la météo dehors'), 'meteo')
        self.assertEqual(nlp.analyze('quelle sera la météo demain matin?'), 'meteo futur')
        self.assertEqual(nlp.analyze("Est-ce que j'ai pris mes médicaments"), 'medicament')
        self.assertEqual(nlp.analyze("Quel est mon horaire"), 'meeting')
        self.assertEqual(nlp.analyze('ou sont mes contacts'), 'contact')
        self.assertEqual(nlp.analyze('ai-je des activités'), 'activite')
        self.assertEqual(nlp.analyze('Quel est mon docteur'), 'medecin')
        
    def test_motClef(self):
        self.assertEqual(nlp.motClef('quel heure est-il'), 'heure')
        self.assertEqual(nlp.motClef('quelle est la météo dehors'), 'meteo')
        self.assertEqual(nlp.motClef('quelle sont les prévisions demain matin?'), 'meteo futur')
        self.assertEqual(nlp.motClef("Est-ce que j'ai pris mes médicaments"), 'medicament')
        self.assertEqual(nlp.motClef("Quel est mon horaire"), 'meeting')
        self.assertEqual(nlp.motClef('ou sont mes contacts'), 'contact')
        self.assertEqual(nlp.motClef('ai-je des activités'), 'activite')
        self.assertEqual(nlp.motClef('Quel est mon docteur'), 'medecin')
    

if __name__ == '__main__':
    unittest.main()