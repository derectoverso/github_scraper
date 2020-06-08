# -*- coding: utf-8 -*-
# Github Scraper
# Version 1.0.0
# Date: 07/June/2020

import requests
import sys
from bs4 import BeautifulSoup

from scrapers.repository import scrape_repositories_search

def show_program_title():
    print('\n==== Github Scraper ====')
    print(' Version 1.0.0')
    print(' Last update: June 2020 ')
    print('========================\n')


if __name__ == '__main__':
    show_program_title()

    if len(sys.argv) < 4:
        exit("Not enough arguments")

    scraping_type = sys.argv[1]

    if scraping_type.lower() in ["repo", "repos", "repository", "repositories"]:
        scraping_type = 1
    elif scraping_type.lower() in ["contrib", "contributor", "contributors"]:
        scraping_type = 2
    else:
        exit("Wrong scraping type")

    keywords = sys.argv[2].split(",")

    max_results = sys.argv[3]

    print(scraping_type)
    print(keywords)
    print(max_results)

    print("\nReady to start scraping!")

    if scraping_type == 1:
        scrape_repositories_search(keywords, int(max_results))
    
