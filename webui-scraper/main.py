from scraper import Scraper
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
            print(f"Number of submitted queries: {len(self.queries)}")
            print("")
            for i, query in enumerate(self.queries):
                print(f"Query number {i}:")
                print(f"    - Content: {query.content}")
                print(f"    - Language: {query.lang}")


if __name__ == "__main__":
    app = App()

    queries = [
        Query("Oggi il sole splende e il cielo è sereno.", app.debug),             # Italiano, IT
        Query("The quick brown fox jumps over the lazy dog.", app.debug),          # Inglese, EN
        Query("Demain, il fera beau et nous irons au marché.", app.debug),         # Francese, FR
        Query("La biblioteca está cerrada durante el fin de semana.", app.debug),  # Spagnolo, ES
        Query("Der Winter ist kalt, aber auch sehr schön.", app.debug),            # Tedesco, DE
        Query("O café da manhã foi delicioso hoje.", app.debug),                   # Portoghese, PT
        Query("De kinderen spelen buiten in de tuin.", app.debug),                 # Olandese, NL
        Query("Сегодня вечером будет очень холодно.", app.debug),                  # Russo, RU
        Query("今天的天气非常好。", app.debug),                                      # Cinese, ZH
        Query("今日は学校に行きます。", app.debug),                                   # Giapponese, JA
        Query("السماء صافية اليوم والشمس مشرقة.", app.debug)                     # Arabo, AR
    ]
    
    app.submit_queries(queries)
