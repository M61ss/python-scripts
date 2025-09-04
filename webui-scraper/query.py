from lingua import Language, LanguageDetectorBuilder

class Query:
    def __init__(self, content):
        self.content = content
        self.lang = self.__detect_language()

    def __detect_language(self):
        detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()
        language : Language = detector.detect_language_of(self.content)
        return language.iso_code_639_1.name
    