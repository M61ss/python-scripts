from scraper import Scraper
from query import Query
import sys
from nlp import NLP

class App:
    def __init__(self):
        self.debug = True if "--debug" in sys.argv else False
        self.queries = []

    def retrive_scraping(self):
        scraper = Scraper(self.debug)
        outputs = []
        for query in self.queries:
            query_output = scraper.scrape(query)
            if self.debug:
                print(f"Output for query {query}:\n{query_output}")
            outputs.append(query_output)

    def submit_queries(self, queries : Query):
        self.queries.extend(queries)
        if self.debug:
            for i, query in enumerate(self.queries):
                print(f"Query number {i}:")
                print(f"    - Content: {query.content}")
                print(f"    - Language: {query.lang}")
            print("")
            print(f"Total number of submitted queries: {len(self.queries)}")


if __name__ == "__main__":
    app = App()
    nlp = NLP(app.debug)

    queries = [
        Query("Oggi il sole splende e il cielo è sereno.", nlp),             # Italiano, IT
        Query("The quick brown fox jumps over the lazy dog.", nlp),          # Inglese, EN
        Query("Demain, il fera beau et nous irons au marché.", nlp),         # Francese, FR
        Query("La biblioteca está cerrada durante el fin de semana.", nlp),  # Spagnolo, ES
        Query("Der Winter ist kalt, aber auch sehr schön.", nlp),            # Tedesco, DE
        Query("O café da manhã foi delicioso hoje.", nlp),                   # Portoghese, PT
        Query("De kinderen spelen buiten in de tuin.", nlp),                 # Olandese, NL
        Query("Сегодня вечером будет очень холодно.", nlp),                  # Russo, RU
        Query("今天的天气非常好。", nlp),                                      # Cinese, ZH
        Query("今日は学校に行きます。", nlp),                                   # Giapponese, JA
        Query("السماء صافية اليوم والشمس مشرقة.", nlp)                     # Arabo, AR
    ]
    
    app.submit_queries(queries)
