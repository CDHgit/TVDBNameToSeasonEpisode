from bs4 import BeautifulSoup
from collections import defaultdict


def dict_from_resp(response):
    season_episode_dict = defaultdict(list)
    soup = BeautifulSoup(response.text, features="html.parser")
    show_title = remove_whitespaces(remove_tags(str(soup.h2.a)))
    print(show_title)
    entire_season = soup.table
    season_number = header_to_season(str(soup.h3))
    while entire_season:
        episode_in_season = entire_season.tbody.tr

        while episode_in_season:
            episode_number_html = episode_in_season.td
            episode_name_html = episode_number_html.next_sibling.next_sibling
            # if season_number:
                # print("SEASON: " + season_number)
            if episode_number_html:
                episode_number = remove_whitespaces(remove_tags(str(episode_number_html)))
                # print("NUMBER: " + episode_number)
            if episode_name_html:
                episode_name = remove_whitespaces(remove_tags(remove_whitespaces(str(episode_name_html.span))))
            #     print("NAME: " + episode_name)
            # print()
            if season_number and episode_number and episode_name:
                season_episode_dict[season_number].append((episode_number, episode_name))
            episode_in_season = episode_in_season.next_sibling.next_sibling
        entire_season = entire_season.next_sibling.next_sibling
        season_number = header_to_season(str(entire_season))
        try:
            entire_season = entire_season.next_sibling.next_sibling
        except AttributeError:
            break
    return show_title, season_episode_dict


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
