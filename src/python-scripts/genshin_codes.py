"""
requests is used to send HTTP requests to retrieve web content
bs4 (BeautifulSoup) is used to parse the HTML file of the web page
"""
import requests
from bs4 import BeautifulSoup

def is_code(a_string: str) -> bool:
    """
    Determines whether a string contains whitespaces in between words.

    :args: a_string (str): any string
    :returns: a boolean value:
    """

    return not any(character.isspace() for character in a_string.strip())

def find_codes_and_rewards(soup: BeautifulSoup) -> dict[str, list[str]]:
    """
    Extracts promo codes and their associated rewards from the provided BeautifulSoup object.

    :args: soup (BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

    :returns: dict[str, list[str]]: A dictionary where keys are promo codes (str)\
         and values are lists of rewards (list[str]).
    """

    cumulative_codes_list = []
    cumulative_rewards_list = []
    td_list = soup.find_all('td', attrs={'data-sort-val': True})
    for td_tag in td_list:
        code = td_tag.parent.contents[1]
        if is_code(code.text): # if the code contains words, it is excluded from the list
            cumulative_codes_list.append(code.text.rstrip('\n'))
        item_list = td_tag.parent.find_all('span', class_='item')
        rewards_list = []
        for item in item_list:
            rewards_list.append(item.text.strip().replace('\u00d7', 'x'))
        cumulative_rewards_list.append(rewards_list)
    return dict(zip(cumulative_codes_list, cumulative_rewards_list))

def print_out(cumulative_dict: dict) -> None:
    """
    Prints the promo codes and their rewards in a formatted manner for the discord bot to print.

    :args: cumulative_dict (dict[str, list[str]]): A dictionary where keys\
         are promo codes (str) and values are lists of rewards (list[str]).
    """

    print(f'There are {len(cumulative_dict)} codes available to redeem:\n')
    for codes, rewards in cumulative_dict.items():
        print(f'{codes} - {", ".join(rewards)}')
    print('\nRedeem the codes here: https://genshin.hoyoverse.com/en/gift')

def main() -> None:
    """
    Main function that retrieves the webpage, parses it, and prints the promo codes and rewards.
    """

    url = 'https://genshin-impact.fandom.com/wiki/Promotional_Code'
    response = requests.get(url, timeout=60)
    soup = BeautifulSoup(response.text, 'html.parser')

    cumulative_dict = find_codes_and_rewards(soup)
    print_out(cumulative_dict)

if __name__ == '__main__':
    main()
