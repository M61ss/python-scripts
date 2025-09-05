import wikipedia
from query import Query

class Scraper:
    def __init__(self, debug : bool = False):
        self.debug : bool = debug

    def scrape(self, query : Query):
        results = wikipedia.search(query.content)
        if self.debug:
            print(f"Start research on Wikipedia about: {query.content}")
            for i, result in enumerate(results[:3]):
                print(f"- {i}: {result}")