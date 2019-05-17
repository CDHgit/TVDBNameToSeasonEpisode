import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def scrape_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    boldHeadings = soup.h3
    while boldHeadings:
        print(boldHeadings)
        entireSeason = boldHeadings.parent
        print(entireSeason)
        boldHeadings = boldHeadings.next_sibling
