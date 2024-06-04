"""Module providing return type hint to functions"""
from typing import List
import requests
from bs4 import BeautifulSoup
from bs4 import Tag

def find_ul_tags(soup: BeautifulSoup) -> List[Tag]:
    """
    Finds and returns all 'ul' tags inside the first 'div' with class 'entry-content'

    :param soup: BeautifulSoup object representing the parsed HTML
    :return: List of 'ul' Tag objects
    """

    target_tag = soup.find('div', class_='entry-content')
    target_ul = target_tag.find_all('ul')
    return target_ul

def print_codes(target_ul: List[Tag]) -> None:
    """
    Finds and prints all the 'li' tags within the first target_ul tag list object

    :param target_ul:
    """

    number_of_codes = 0
    for li_tag in target_ul[0].find_all('li'):
        number_of_codes += 1
    print(f'There are {number_of_codes} new codes avaliable:\n')
    for li_tag in target_ul[0].find_all('li'):
        msg_array = str(li_tag.text).split('–')
        print(f"{li_tag.find('strong').text.strip()} - {msg_array[1].replace("’", "'").strip()}")
    print('\nRedeem the codes here: https://hsr.hoyoverse.com/gift')

def main():
    """
    Finds the honkai star rail codes
    """

    url = 'https://www.pockettactics.com/honkai-star-rail/codes'
    status = requests.get(url, timeout=60)
    soup = BeautifulSoup(status.text, 'html.parser')

    all_target_uls = find_ul_tags(soup)
    print_codes(all_target_uls)

if __name__ == "__main__":
    main()
