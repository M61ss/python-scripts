import wikipedia
from query import Query

class Scraper:
    def __init__(self, debug : bool = False):
        self.debug : bool = debug

    def scrape(self, query : Query):
        keywords = query.keywords[:3]
        if self.debug:
            print(f"Search results for query '{query.content}':")
            print(f"Keywords: {keywords}")
        for i, keyword in enumerate(keywords):
            results = wikipedia.search(keyword[0])
            if len(results) == 0:
                print(f"No results from Wikipedia for keyword '{keyword}'")
            if self.debug:
                for j, result in enumerate(results[:3]):
                    print(f"- {i + 1}.{j + 1}: {result}")