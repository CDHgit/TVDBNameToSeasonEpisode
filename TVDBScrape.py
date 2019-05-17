import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def scrape_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    entireSeason = soup.table
    season_number = header_to_season(str(soup.h3))
    print("FIRSTSEASONNUM" + season_number)
    while entireSeason:
        episodeInSeason = entireSeason.tbody.tr

        while episodeInSeason:
            episodeNumber = episodeInSeason.td
            episodeName = episodeNumber.next_sibling.next_sibling
            if season_number:
                print("SEASON: " + season_number)
            if episodeNumber:
                print("NUMBER: " + remove_whitespaces(remove_tags(str(episodeNumber))))
            if episodeName:
                print("NAME: " + remove_whitespaces(remove_tags(remove_whitespaces(str(episodeName.span)))))
            print()

            episodeInSeason = episodeInSeason.next_sibling.next_sibling
        entireSeason = entireSeason.next_sibling.next_sibling
        season_number = header_to_season(str(entireSeason))
        try:
            entireSeason = entireSeason.next_sibling.next_sibling
        except AttributeError:
            break


def header_to_season(header_tag):
    space_idx = header_tag.find(' ')
    if space_idx > 0:
        next_bracket_idx = header_tag.find('<', space_idx)
        return header_tag[space_idx + 1:next_bracket_idx]
    else:
        return remove_tags(header_tag)


def remove_tags(html_tag):
    num_tags = html_tag.count('<')  # Breaks on strings with <
    close_bracket_idx = 0
    for x in range(int(num_tags/2)):
        open_bracket_idx = html_tag.find('<', close_bracket_idx)
        close_bracket_idx = html_tag.find('>', open_bracket_idx)
    open_bracket_idx = html_tag.find('<', close_bracket_idx)
    return html_tag[close_bracket_idx + 1:open_bracket_idx]


def remove_whitespaces(input_string):
    input_string = input_string.strip()
    input_string = input_string.replace("\n", "")
    return input_string




