import wikipedia
from query import Query

class Scraper:
    def __init__(self, debug : bool = False):
        self.debug : bool = debug

    def search(self, query : Query):
        keywords = query.keywords[:2]
        results = []
        if self.debug:
            print(f"Search results for query '{query.content}':")
            print(f"Keywords: {keywords}")
        for i, keyword in enumerate(keywords):
            curr_results = wikipedia.search(keyword[0])
            if self.debug:
                if len(curr_results) == 0:
                    print(f"No results from Wikipedia for keyword '{keyword}'")
                for j, result in enumerate(curr_results[:3]):
                    print(f"- {i + 1}.{j + 1}: {result}")
            results.append(curr_results)
        return results

    def scrape(self, query : Query):
        results = self.search(query)
        pages = []
        for result in results:
            try:
                page = wikipedia.page(result)
                pages.append(page)
            except:
                if self.debug:
                    print(f"Page found for search result '{result}':")
                    print(page)
        return pages