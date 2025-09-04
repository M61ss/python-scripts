from bs4 import BeautifulSoup
from selenium import webdriver
from query import Query

class Scraper:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def scrape(self, query : Query):
        self.driver.get(f"https://www.google.com/ / search?q = {query.content}")