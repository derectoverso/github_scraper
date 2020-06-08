# Github webscraper
Webscraper for Github repositories and contributors.

This project use Python 3, Requests and BeautifulSoup 4 to scrape and parse Github pages.

**Privacy Notice: This tool download the results to a local file. The data is never linked to a a database or other services.**


## Dependencies

Python 3.7
 - sys
 - requests
 - BeautifulSoup 4


## Usage

``` > python main.py 'scraping_type' 'keywords' ```

Scraping types available: [repositories]

Keywords: List of coma-separated keywords to use to search for repositories

``` > python main.py repositories python,scrapers ```

 ## Result
 
 A list of multiple repositories with the following informations:
 
    "title": "",
    "contributor": "",
    "url": "",
    "description": "",
    "tags": [],
    "stars": "",
    "language": "",
    "license": "",
    "update": ""
                