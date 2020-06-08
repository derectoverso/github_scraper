# -*- coding: utf-8 -*-
# Repository scraper
# Version 1.0.0
# Date: 07/June/2020

import requests
import sys

from bs4 import BeautifulSoup
from tools import csv

# Use Requests to get search page's content
def get_search_page_content(keywords_array, page=0):

    if page == 0:
        github_url = "https://github.com/search?q="
    elif page > 0:
        github_url = "https://github.com/search?p="+str(page)+"&q="

    for keyword in keywords_array:
        github_url = github_url + keyword + "+"
    
    github_url = github_url[:-1]

    print("\nSraping URL " + github_url)

    search_request = None
    try:
        search_request = requests.get(github_url, timeout=10, allow_redirects=False)
    except requests.exceptions.Timeout as timeout:
        print(timeout)
    except requests.exceptions.RequestException as error:
        print(error)
    
    if search_request is not None:
        search_request = search_request.content

    return search_request

# Use BeautifulSoup to parse search's page content
def parse_search_page_content(page_content, max_repositories=10):
    repos_array = []

    if page_content is None:
        print("No page content")
    
    soup = BeautifulSoup(page_content, "html5lib", from_encoding='utf-8')
    if soup is not None:
        repo_list = soup.find("ul", {"class": ["repo-list"]})
        if repo_list is not None:
            repo_items = repo_list.find_all("li", {"class": ["repo-list-item"]})

            for repo in repo_items:
                repo_array = {
                    "title": "",
                    "contributor": "",
                    "url": "",
                    "description": "",
                    "tags": [],
                    "stars": "",
                    "language": "",
                    "license": "",
                    "update": ""
                }

                content = repo.find("div", {"class": "mt-n1"})
                if content is not None:

                    # Title , Contributor , URL
                    title_container = content.find("div", {"class": ["f4"]})
                    if title_container is not None:
                        title_link = title_container.find("a")
                        if title_link is not None:
                            link = title_link.get("href")
                            if link is not None:
                                repo_array["url"] = "https://www.github.com" + link

                                contributor_title = link.split("/")
                                repo_array["contributor"] = contributor_title[1]
                                repo_array["title"] = contributor_title[2]

                    # Description
                    description_container = content.find("p", {"class": ["mb-1"]})
                    if description_container is not None:
                        description = description_container.get_text()
                        description = description.replace("\n", "").strip()
                        repo_array["description"] = description
                    
                    # Tags
                    tags = content.find_all("a", {"class": ["topic-tag"]})
                    for tag in tags:
                        repo_array["tags"].append(tag.get_text().strip())

                    # Stars , Language , License , Last update
                    information_container = content.find("div", {"class": ["d-flex"]})
                    if information_container is not None:
                        # Stars
                        stars_container = information_container.find("a", {"class": ["muted-link"]})
                        if stars_container is not None:
                            repo_array["stars"] = stars_container.get_text().strip()
                        
                        # Languages
                        language_container = information_container.find("span", {"itemprop": ["programmingLanguage"]})
                        if language_container is not None:
                            repo_array["language"] = language_container.get_text().strip()

                        # License
                        div_mr3 = information_container.find_all("div", {"class": ["mr-3"]})
                        if len(div_mr3) == 4:
                            repo_array["license"] = div_mr3[2].get_text().strip()

                        # Update
                        update_container = information_container.find("relative-time")
                        if update_container is not None:
                            repo_array["update"] = update_container.get("datetime")

                repos_array.append(repo_array)

    return repos_array


# Scrape a number of repositories based on a keyword search
def scrape_repositories_search(keywords_array, max_repositories=10):

    # Scrape first page 
    search_content = get_search_page_content(keywords_array, 0)

    repositories = parse_search_page_content(search_content)

    # Write CSV header with initial results
    csv.write_header_to_csv("output/search.csv", repositories[0].keys())
    # Write CSV body with initial results
    csv.write_dict_to_csv("output/search.csv", repositories)

    # Parse next pages and scrape results
    for page in range(2, int(max_repositories / 10)+1):
        search_content = get_search_page_content(keywords_array, page)

        repositories = parse_search_page_content(search_content)

        csv.write_dict_to_csv("output/search.csv", repositories)
        


