"""
This module contains translation functions for converting English text to French and vice versa.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translates English text to French using the MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates French text to English using the MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    print(english_text)
    return english_text
