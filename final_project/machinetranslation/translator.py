
from deep_translator import GoogleTranslator

def english_to_french(english_text):
    """Translate from english to french using GGtranslator"""
    french_text = GoogleTranslator(source='english', target='french').translate(text=english_text)
    return french_text

def french_to_english(french_text):
    """Translate from french to english using GGtranslator"""
    english_text = GoogleTranslator(source='french', target='english').translate(text=french_text)
    return english_text
