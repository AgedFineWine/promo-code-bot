"""
re is used to create regular expressions to remove parts of a string
requests is used to send HTTP requests to retrieve web content
bs4 (BeautifulSoup) is used to parse the HTML file of the web page
"""
import re

import requests
from bs4 import BeautifulSoup

def find_codes_and_rewards(soup: BeautifulSoup) -> dict[str, list[str]]:
    """
    Extracts promo codes and their associated rewards from the provided BeautifulSoup object.

    :args: soup (BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

    :returns: dict[str, list[str]]: A dictionary where keys are promo codes (str)\
         and values are lists of rewards (list[str]).
    """
    cumulative_codes_list = []
    cumulative_rewards_list = []
    table = soup.find('table', class_='wikitable')
    tr_list = table.find_all('tr')
    tr_list.pop(0)
    for tr_tag in tr_list:
        code = tr_tag.contents[1]
        cumulative_codes_list.append(code.text.rstrip('\n'))
        item_element = tr_tag.contents[5].text.rstrip('\n')
        cumulative_rewards_list.append(re.sub(r'\[\d*\]', '', item_element))

    return dict(zip(cumulative_codes_list, cumulative_rewards_list))

def print_out(cumulative_dict: dict) -> None:
    """
    Prints the promo codes and their rewards in a formatted manner for the discord bot to print.

    :args: cumulative_dict (dict[str, list[str]]): A dictionary where keys\
         are promo codes (str) and values are lists of rewards (list[str]).
    """
    print(f'There are {len(cumulative_dict)} codes available to redeem:\n')
    for codes, rewards in cumulative_dict.items():
        print(f'{codes} - {rewards}')
    print('\nTo redeem these codes go to the store page or your profile at the Wizard homepage.')

def main() -> None:
    """
    Main function that retrieves the webpage, parses it, and prints the promo codes and rewards.
    """
    url = 'https://mtg.fandom.com/wiki/Magic:_The_Gathering_Arena/Promotional_codes'
    response = requests.get(url, timeout=60)
    soup = BeautifulSoup(response.text, 'html.parser')

    cumulative_dict = find_codes_and_rewards(soup)
    print_out(cumulative_dict)

if __name__ == '__main__':
    main()
