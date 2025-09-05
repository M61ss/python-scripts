from scraper import Scraper
from nlp import NLP
from query import Query
import sys

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
                print(f"    - Keywords: {query.keywords}")
            print("")
            print(f"Total number of submitted queries: {len(self.queries)}")


if __name__ == "__main__":
    app = App()
    nlp = NLP(app.debug)

    queries = [
        nlp.compose_query("Oggi il sole splende e il cielo è sereno."),             # Italiano, IT
        nlp.compose_query("The quick brown fox jumps over the lazy dog."),          # Inglese, EN
        nlp.compose_query("Demain, il fera beau et nous irons au marché."),         # Francese, FR
        nlp.compose_query("La biblioteca está cerrada durante el fin de semana."),  # Spagnolo, ES
        nlp.compose_query("Der Winter ist kalt, aber auch sehr schön."),            # Tedesco, DE
        nlp.compose_query("O café da manhã foi delicioso hoje."),                   # Portoghese, PT
        nlp.compose_query("De kinderen spelen buiten in de tuin."),                 # Olandese, NL
        nlp.compose_query("Сегодня вечером будет очень холодно."),                  # Russo, RU
        nlp.compose_query("今天的天气非常好。"),                                      # Cinese, ZH
        nlp.compose_query("今日は学校に行きます。"),                                   # Giapponese, JA
        nlp.compose_query("السماء صافية اليوم والشمس مشرقة."),                    # Arabo, AR
    ]
    
    app.submit_queries(queries)
