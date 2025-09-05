from lingua import Language, LanguageDetectorBuilder
from keybert import KeyBERT
from query import Query

class NLP:
    def __init__(self, debug = False):
        self.debug = debug
        self.detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()
        self.kw_model = KeyBERT()

    def compose_query(self, content : str):
        query_lang = self.__detect_language(content)
        query_keywords = self.__extract_keywords(content)
        return Query(content, query_lang, query_keywords)

    def __detect_language(self, content : str):
        language : Language = self.detector.detect_language_of(content)
        if self.debug:
            print(f"Detected language for query '{content}': {language.iso_code_639_1.name}")
        return language.iso_code_639_1.name
    
    def __extract_keywords(self, content : str):
        return self.kw_model.extract_keywords(content)