import requests
from bs4 import BeautifulSoup

"""MAKE THE WORLD HONEST AGAIN

This file is used to determine the reliability index of a news article by comparing it to news articles with existing
reliability indices.

The process will start by building a dataset of articles with pre-defined indices. Then it will take the inputted news
article and compare its contents with related articles and calculate its corresponding reliability index.

"""

"""This section will be used for creating and updating the database of urls."""
URL_DATABASE = {}


def add_url(url: str, index: float = -1) -> None:
    """This function adds the url with its reliability index to the URL_DATABASE. The reliability index is a float
    from 0 to 1 or set to -1 if undefined."""
    if url in URL_DATABASE:
        URL_DATABASE[url] = {index}
    else:
        URL_DATABASE[url].add(index)


def add_urls(urls: set) -> None:
    """This function adds all the urls in urls to URL_DATABASE."""
    for url in urls:
        add_url(url)


"""This section will be used for calculating the reliability index of a url."""


def compare(url1: str, url2: str) -> float:
    """This function takes two news articles with urls url1 and url2 and returns a reliability index for url1
    between 0 and 1 by comparing it to the contents of url2 and its given reliability index."""


