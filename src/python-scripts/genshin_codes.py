"""Module providing return type hint to functions"""
from typing import List
from bs4 import BeautifulSoup
from bs4 import Tag
import requests

def find_li_tags(soup: BeautifulSoup) -> List[Tag]:
    """
    Finds and returns all 'li' tags within the first 'ul' tag
    inside the 'div' with class 'entry-content'.

    :param soup: BeautifulSoup object representing the parsed HTML.
    :return: List of 'li' Tag objects.
    """

    ancestor_tag = soup.find('div', class_="entry-content")
    first_ul_tag = ancestor_tag.find('ul')
    li_tags = first_ul_tag.find_all('li')
    return li_tags

def print_codes(li_tags: List[Tag]) -> None:
    """
    Prints the number of codes and the text within each 'li' tag.

    :param li_tags: List of 'li' Tag objects.
    """
    number_of_codes = 0
    for li_tag in li_tags:
        number_of_codes += 1
    print(f'There are {number_of_codes} new Genshin Impact codes avaliable:\n')
    for li_tag in li_tags:
        print(li_tag.text.replace("–", "-"))
    print('\nRedeem the codes here: https://hsr.hoyoverse.com/gift')

def main():
    """
    Finds the genshin impact codes
    """
    url = "https://www.pockettactics.com/genshin-impact/codes"
    status = requests.get(url, timeout=60)
    soup = BeautifulSoup(status.text, 'html.parser')

    li_tags = find_li_tags(soup)
    print_codes(li_tags)

if __name__ == "__main__":
    main()
