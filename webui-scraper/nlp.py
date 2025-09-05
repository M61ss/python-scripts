from lingua import Language, LanguageDetectorBuilder
from keybert import KeyBERT

class NLP:
    def __init__(self, debug = False):
        self.debug = debug
        self.detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()

    def detect_language(self, content):
        language : Language = self.detector.detect_language_of(content)
        if self.debug:
            print(f"Detected language for query '{content}': {language.iso_code_639_1.name}")
        return language.iso_code_639_1.name
    
    def extract_keywords(self, content):
        pass