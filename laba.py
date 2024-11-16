""" Lab A: Web Scraping

Crawls the website http://books.toscrape.com and creates a spreadsheet of books.
"""
import time
import random
import requests
import json
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup as Soup, BeautifulSoup

# User Agent from Chrome Browser on Win 10/11
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

DEFAULT_SLEEP = 3.0 # These may need tuning
SIGMA = 1.0

DOMAIN = 'http://books.toscrape.com' # Ideally, these would be
STATE_FILENAME = 'state.json'        # read in from a configuration
OUTPUT_FILENAME = 'books.csv'        # or commandline, but this is fine


def get(url: str) -> requests.Response:
    """Waits a random amount of time, then send a GET request"""
    time.sleep(random.gauss(DEFAULT_SLEEP, SIGMA))
    return requests.get(url, headers=HEADERS)


# [TODO] Save links left to visit and the data extracted to a JSON file
def save_state(filename: str, links: list[str], data: dict[str, dict]) -> None:
    with open(filename, 'w') as f:
        json.dump({'links': links, 'data': data}, f)

# [TODO] Load links left to visit and collected data from a JSON file
def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    with open(filename, 'r') as f:
        state = json.load(f)
        return state['links'], state['data']

# [TODO] Write all data to a CSV file
def write_spreadsheet(filename: str, data: dict[str, dict]) -> None:
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        names = ['title', 'category', 'upc', 'price', 'tax', 'availability', 'reviews']
        sheet = csv.DictWriter(f, fieldnames=names)
        sheet.writeheader()
        for book in data.values():
            sheet.writerow(book)

