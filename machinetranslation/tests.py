import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from machinetranslation import translator

class TranslationTests(unittest.TestCase):
    
    def test_french_to_english(self):
        french_text = "Bonjour"
        expected_translation = "Hello"
        translation = translator.french_to_english(french_text)
        self.assertEqual(translation, expected_translation)
        self.assertNotEqual(translation, french_text)

    def test_english_to_french(self):
        english_text = "Hello"
        expected_translation = "Pepitoooo"  # Assuming no translation available
        translation = translator.english_to_french(english_text)
        self.assertEqual(translation, expected_translation)
        self.assertNotEqual(translation, english_text)
        
    
if __name__ == '__main__':
    unittest.main()

