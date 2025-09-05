import wikipedia
from query import Query

class Scraper:
    def __init__(self, debug : bool = False):
        self.debug : bool = debug

    def set_language(self, query : Query):
        query_lang : str = query.lang.lower()
        if query_lang in wikipedia.languages():
            wikipedia.set_lang(query_lang)
            if self.debug:
                print(f"Wikipedia API language set on: {query_lang}")
        else:
            if self.debug:
                print(f"Language {query_lang} is not supported by Wikipedia. Wikipedia API language not set.")

    def search(self, query : Query):
        self.set_language(query)
        keywords = query.keywords[:2]
        results = []
        if self.debug:
            print(f"Search results for query '{query.content}':")
            print(f"Keywords: {keywords}")
        for i, keyword in enumerate(keywords):
            curr_results = wikipedia.search(keyword[0], results=3)
            if self.debug:
                if len(curr_results) == 0:
                    print(f"No results from Wikipedia for keyword '{keyword}'")
                for j, result in enumerate(curr_results):
                    print(f"- {i + 1}.{j + 1}: {result}")
            results.extend(curr_results)
        return results

    def scrape(self, query : Query):
        results = self.search(query)
        pages = []
        for result in results:
            try:
                page : wikipedia.WikipediaPage = wikipedia.page(result)
                if self.debug:
                    print(f"Page found for '{result}':")
                    print(f"Page summary: {page.summary}")
                pages.append(page)
            except:
                if self.debug:
                    print(f"Page NOT found for '{result}'")
        return pages