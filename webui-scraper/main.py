from scraper import Scraper
from nlp import NLP
from query import Query
import sys

class App:
    def __init__(self, nlp : NLP, debug : bool = False):
        self.nlp = nlp
        self.debug = debug

    def __retrive_scraping(self, query : Query):
        scraper = Scraper(self.debug)
        outputs = []
        query_output = scraper.scrape(query)
        if self.debug:
            print(f"Output for query {query.content}:\n{query_output}")
        outputs.append(query_output)
        return outputs

    def submit_queries(self, query_content : str):
        query : Query = self.nlp.compose_query(query_content)
        if self.debug:
            print(f"Query information:")
            print(f"    - Content: {query.content}")
            print(f"    - Language: {query.lang}")
            print(f"    - Keywords: {query.keywords}")
        return self.__retrive_scraping(query)

if __name__ == "__main__":
    debug = True if "--debug" in sys.argv else False
    
    nlp = NLP(debug)
    app = App(nlp, debug)

    query_contents = [
        "Oggi il sole splende e il cielo è sereno.",             # Italiano, IT
        "The quick brown fox jumps over the lazy dog.",          # Inglese, EN
        "Demain, il fera beau et nous irons au marché.",         # Francese, FR
        "La biblioteca está cerrada durante el fin de semana.",  # Spagnolo, ES
        "Der Winter ist kalt, aber auch sehr schön.",            # Tedesco, DE
        "O café da manhã foi delicioso hoje.",                   # Portoghese, PT
        "De kinderen spelen buiten in de tuin.",                 # Olandese, NL
        "Сегодня вечером будет очень холодно.",                  # Russo, RU
        "今天的天气非常好。",                                      # Cinese, ZH
        "今日は学校に行きます。",                                   # Giapponese, JA
        "السماء صافية اليوم والشمس مشرقة.",                    # Arabo, AR
    ]
    
    for query_content in query_contents:
        app.submit_queries(query_content)
