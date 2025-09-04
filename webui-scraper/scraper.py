import wikipedia
from query import Query

class Scraper:
    def __init__(self):
        pass

    def scrape(self, query : Query):
        print(f"Start research on Wikipedia about: {query.content}")
        results = wikipedia.search(query.content)
        for i, result in enumerate(results[:3]):
            print(f"- {i}: {result}")