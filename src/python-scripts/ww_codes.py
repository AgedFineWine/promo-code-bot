"""
requests is used to send HTTP requests to retrieve web content
bs4 (BeautifulSoup) is used to parse the HTML file of the web page
"""
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
    td_list = soup.find_all('td', class_='bg-new')
    for td_tag in td_list:
        code = td_tag.parent.contents[1]
        cumulative_codes_list.append(code.text)
        item_list = td_tag.parent.find_all('a', attrs={'title': True})
        rewards_list = []
        for item in item_list:
            item_element = item.attrs['title']
            rewards_list.append(item_element.replace('.png', '').replace('File:', '').strip())
        cumulative_rewards_list.append(rewards_list)
    return dict(zip(cumulative_codes_list, cumulative_rewards_list))

def print_out(cumulative_dict: dict) -> None:
    """
    Prints the promo codes and their rewards in a formatted manner for the discord bot to print.

    :args: cumulative_dict (dict[str, list[str]]): A dictionary where keys\
         are promo codes (str) and values are lists of rewards (list[str]).
    """

    print(f'There are {len(cumulative_dict)} new codes available to redeem:\n')
    for codes, rewards in cumulative_dict.items():
        print(f'{codes} - {', '.join(rewards)}')
    print('\nTo redeem these codes log into your account and \
go to "Other settings" from your account settings.')

def main() -> None:
    """
    Main function that retrieves the webpage, parses it, and prints the promo codes and rewards.
    """

    url = 'https://wutheringwaves.fandom.com/wiki/Redemption_Code'
    response = requests.get(url, timeout=60)
    soup = BeautifulSoup(response.text, 'html.parser')

    cumulative_dict = find_codes_and_rewards(soup)
    print_out(cumulative_dict)

if __name__ == '__main__':
    main()
