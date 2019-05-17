import requests


def request_from_url(url):
    response = requests.get(url)
    return response
