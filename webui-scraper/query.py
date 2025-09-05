from nlp import NLP

class Query:
    def __init__(self, content, nlp : NLP):
        self.content = content
        self.lang = nlp.detect_language(self.content)
        self.keywords = nlp.extract_keywords(self.content)  