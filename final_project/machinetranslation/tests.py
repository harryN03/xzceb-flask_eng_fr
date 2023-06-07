import unittest

from translator import english_to_french,french_to_english
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertEqual(english_to_french("Monday"), "Lundi")
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Good morning") 
        self.assertEqual(french_to_english("lundi"), "Monday") 
        
unittest.main()