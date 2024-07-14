"""
Created by Ignorant on 2024/7/13
Description: Crawler for the Blog Website
"""
import re

import requests
from bs4 import BeautifulSoup as bs

from PythonBasis.Chapter13_Crawler.utils import url_manager


def get_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Failed to get page")

    html_doc = response.text
    soup = bs(html_doc, 'html.parser')

    h2_nodes = soup.find_all('h2', class_="entry-title")
    for h2_node in h2_nodes:
        link = h2_node.find('a')
        print(link.get('href'), link.get_text())


def get_all_pages(url):
    manager = url_manager.UrlManager()
    manager.add_url(url)
    while manager.has_url():
        current_page = manager.get_url()
        response = requests.get(current_page, timeout=10)
        if response.status_code != 200:
            print("Failed to get page:", current_page)
            continue
        soup = bs(response.text, 'html.parser')
        title = soup.title.string
        with open("all_pages_title.txt", "a", encoding="utf-8") as f:
            f.write(f'{current_page}\t{title}\n')
        print(f'Success: {current_page}, {title}')

        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            pattern = r'^https?://www.crazyant.net/\d+.html$'
            if re.match(pattern, href):
                manager.add_url(href)


if __name__ == '__main__':
    url = "http://www.crazyant.net"
    get_all_pages(url)
