from TVDBScrape import scrape_from_url

if __name__ == "__main__":
    urlToScrape = "https://www.thetvdb.com/series/spongebob-squarepants/seasons/all"
    scrape_from_url(urlToScrape)#, features="html.parser")
