"""Module providing return type hint to functions"""
from typing import List
import requests
from bs4 import BeautifulSoup
from bs4 import Tag

def find_tr_tags(soup: BeautifulSoup) -> List[Tag]:
    """
    Find all 'tr' tags with class 'active' within a table of class 'codes-table'

    :param soup (BeautifulSoup): The BeautifulSoup object representing the parsed HTML content
    :return: List[Tag]: A list of 'tr' tags with class 'active' found within the specified table
    """
    table_element = soup.find('table', class_='codes-table')
    tr_tags = table_element.find_all('tr', class_='active')
    return tr_tags

def print_codes(tr_tags: List[Tag]) -> None:
    """
    Print out the codes found in the 'tr' tags

    :param tr_tags (List[Tag]): A list of 'tr' tags containing the codes
    """
    number_of_codes = len(tr_tags)
    print(f'There are {number_of_codes} new Wuthering Waves codes available:\n')
    for tr_tag in tr_tags:
        text_array = tr_tag.text.split(' ')
        print(f"{text_array[0]} - {', '.join(text_array[1:])}")
    print('\nTo redeem these codes log into your account and \
go to "Other settings" from your account settings.')

def main() -> None:
    """
    Main function to scrape Wuthering Waves codes from the specified URL and print them

    The function performs the following steps:
    1. Sends a GET request to the specified URL to retrieve the webpage content
    2. Parses the HTML content using BeautifulSoup
    3. Finds and extracts 'tr' tags with class 'active' from the specified table
    4. Prints out the extracted codes
    """
    url = 'https://wuthering.gg/codes'
    status = requests.get(url, timeout=60)
    soup = BeautifulSoup(status.text, 'html.parser')

    tr_tags = find_tr_tags(soup)
    print_codes(tr_tags)

if __name__ == '__main__':
    main()
