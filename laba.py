""" Lab A: Web Scraping

Crawls the website http://books.toscrape.com and creates a spreadsheet of books.
"""
import time
import random
import requests
import json
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup as Soup

# User Agent from Chrome Browser on Win 10/11
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

DEFAULT_SLEEP = 3.0  # These may need tuning
SIGMA = 1.0

DOMAIN = 'http://books.toscrape.com'
STATE_FILENAME = 'state.json'
OUTPUT_FILENAME = 'books.csv'


def get(url: str) -> requests.Response:
    """Waits a random amount of time, then send a GET request"""
    time.sleep(random.gauss(DEFAULT_SLEEP, SIGMA))
    return requests.get(url, headers=HEADERS)


def save_state(filename: str, links: list[str], data: dict[str, dict]) -> None:
    """Save the state of links to visit and data collected"""
    with open(filename, 'w') as f:
        json.dump({'links': links, 'data': data}, f)


def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    """Load the state of links to visit and data collected"""
    with open(filename, 'r') as f:
        state = json.load(f)
        return state['links'], state['data']


def write_spreadsheet(filename: str, data: dict[str, dict]) -> None:
    """Write the collected book data to a CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        names = ['title', 'category', 'upc', 'price', 'tax', 'availability', 'reviews']
        sheet = csv.DictWriter(f, fieldnames=names)
        sheet.writeheader()
        for book in data.values():
            sheet.writerow(book)


def grab_book_data(soup: Soup) -> dict:
    """Extract book data from the BeautifulSoup object"""
    book_data = {
        'title': soup.find('h1').text.strip() if soup.find('h1') else 'N/A',
        'category': 'N/A',
        'upc': soup.find('th', string='UPC').find_next_sibling('td').text.strip() \
            if soup.find('th', string='UPC') else 'N/A',
        'price': soup.find('th', string='Price (incl. tax)').find_next_sibling('td').text.strip() \
            if soup.find('th', string='Price (incl. tax)') else 'N/A',
        'tax': soup.find('th', string='Tax').find_next_sibling('td').text.strip() \
            if soup.find('th', string='Tax') else 'N/A',
        'availability': soup.find('th', string='Availability').find_next_sibling('td').text.strip() \
            if soup.find('th', string='Availability') else 'N/A',
        'reviews': soup.find('th', string='Number of reviews').find_next_sibling('td').text.strip() \
            if soup.find('th', string='Number of reviews') else 'N/A'
    }

    # Extract category if available
    breadcrumb = soup.find('ul', class_='breadcrumb')
    if breadcrumb:
        li_elements = breadcrumb.find_all('li')
        if len(li_elements) > 2:
            book_data['category'] = li_elements[2].text.strip()

    return book_data


def get_links(soup: Soup, current_url: str, to_visit: list[str], data: dict[str, dict]) -> None:
    """Extract links from the BeautifulSoup object and add to the list of links to visit"""
    for link in soup.find_all('a'):
        full_url = urljoin(current_url, link.get('href'))
        if full_url.startswith(DOMAIN) and full_url not in data and full_url not in to_visit:
            to_visit.append(full_url)


def scrape(url: str, data: dict[str, dict], to_visit: list[str]) -> None:
    """Process the page and extract data and links"""
    response = get(url)
    if response.status_code != 200:
        print(f"Failed to get {url}")
        return
    soup = Soup(response.content, 'html.parser')

    if 'catalogue' in url and 'book' in url:
        book_data = grab_book_data(soup)
        data[url] = book_data
        print(f"Scraped book data from {url}")
    get_links(soup, url, to_visit, data)


if __name__ == '__main__':
    try:
        to_visit, data = load_state(STATE_FILENAME)
    except FileNotFoundError:
        to_visit = ['/index.html']
        data = {}

    # Main Loop
    while len(to_visit) > 0:
        try:
            url = to_visit.pop(0)
            if url not in data:
                print(f"Scraping URL: {url}")
                scrape(url, data, to_visit)
                print(f"Completed scraping: {url}")
        except KeyboardInterrupt:
            save_state(STATE_FILENAME, to_visit, data)
            finished = False
            break
    else:
        finished = True

    if finished:
        print("Writing data to CSV file")
        write_spreadsheet(OUTPUT_FILENAME, data)
        print(f"Finished writing to {OUTPUT_FILENAME}")

