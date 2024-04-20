import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


def scrape_website(url):
    """Scrape the website and return the BeautifulSoup object."""
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to get the page: {e}")
        return None

    return BeautifulSoup(page.text, 'html.parser')


def extract_content(soup):
    """Extract and return the content from the BeautifulSoup object."""
    if soup is None:
        return None

    content_div = soup.find('div', id='caas-content-body')
    if content_div is None:
        logging.error("Couldn't find the content div")
        return None

    return content_div.text.strip()


def main():
    url = "https://finance.yahoo.com/news/inflation-comes-in-hotter-than-expected-in-march-123324666.html"
    soup = scrape_website(url)
    content = extract_content(soup)

    if content is None:
        logging.error("Failed to extract content")

    return content


if __name__ == "__main__":
    print(main())