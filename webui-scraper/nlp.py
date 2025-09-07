from lingua import Language, LanguageDetectorBuilder, LanguageDetector
from keybert import KeyBERT
from query import Query

class NLP:
    def __init__(self, debug : bool = False):
        self.debug : bool = debug
        self.detector : LanguageDetector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()
        self.kw_model : KeyBERT = KeyBERT()

    def compose_query(self, content : str):
        query_lang = self.__detect_language(content)
        if not query_lang:
            query_lang = Language.ENGLISH.iso_code_639_1.name
        query_keywords = self.__extract_keywords(content)
        return Query(content, query_lang, query_keywords)

    def __detect_language(self, content : str):
        language : Language = self.detector.detect_language_of(content)
        lang = language.iso_code_639_1.name if language else None
        if self.debug:
            print(f"Detected language for query '{content}': {lang}")
        return lang
    
    def __extract_keywords(self, content : str):
        return self.kw_model.extract_keywords(content)