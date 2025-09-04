import wikipedia
from query import Query

class Scraper:
    def __init__(self):
        pass

    def scrape(self, query : Query):
        self.driver.get(f"https://www.google.com/ / search?q = {query.content}")