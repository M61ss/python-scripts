from lingua import Language, LanguageDetectorBuilder
from keybert import KeyBERT

class Query:
    def __init__(self, content, debug = False):
        self.debug = debug
        self.content = content
        self.lang = self.__detect_language()

    def __detect_language(self):
        detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()
        language : Language = detector.detect_language_of(self.content)
        if self.debug:
            print(f"Detected language for query '{self.content}': {language.iso_code_639_1.name}")
        return language.iso_code_639_1.name
    