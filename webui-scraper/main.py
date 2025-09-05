from scraper import Scraper
from nlp import NLP
from query import Query
import sys

debug : bool = True if "--debug" in sys.argv else False
nlp : NLP = NLP(debug)

query_contents = [
        "Oggi il sole splende e il cielo è sereno.",             # Italiano, IT
        "The quick brown fox jumps over the lazy dog.",          # Inglese, EN
        "Demain, il fera beau et nous irons au marché.",         # Francese, FR
        "La biblioteca está cerrada durante el fin de semana.",  # Spagnolo, ES
        "Der Winter ist kalt, aber auch sehr schön.",            # Tedesco, DE
        "O café da manhã foi delicioso hoje.",                   # Portoghese, PT
        "De kinderen spelen buiten in de tuin.",                 # Olandese, NL
        "Сегодня вечером будет очень холодно.",                  # Russo, RU
        "今天的天气非常好。",                                      # Cinese, ZH
        "今日は学校に行きます。",                                   # Giapponese, JA
        "السماء صافية اليوم والشمس مشرقة.",                    # Arabo, AR
    ]

if debug:
    print("Start to compose queries...")
    print("")

queries = []
for query_content in query_contents:
    query : Query = nlp.compose_query(query_content)
    if debug:
        print(f"Query information:")
        print(f"    - Content: {query.content}")
        print(f"    - Language: {query.lang}")
        print(f"    - Keywords: {query.keywords}")
    queries.append(query)

if debug:
    print("Start to scrape on Wikipedia using composed queries...")
    print("")

scraper : Scraper = Scraper(debug)
wiki_outputs = []
for query in queries:
    wiki_output = scraper.scrape(query)
    if debug:
        print(f"Output for query {query.content}:\n{wiki_output}")
    wiki_outputs.append(wiki_output)
