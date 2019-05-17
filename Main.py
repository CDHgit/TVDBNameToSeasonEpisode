from TVDBRequest import request_from_url
from ScrapeToDict import dict_from_resp

if __name__ == "__main__":
    urlToScrape = "https://www.thetvdb.com/series/spongebob-squarepants/seasons/all"
    response = request_from_url(urlToScrape)#  features="html.parser")
    show_dict = dict_from_resp(response)
    print(show_dict)



