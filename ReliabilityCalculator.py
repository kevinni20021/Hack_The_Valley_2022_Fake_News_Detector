import requests
from bs4 import BeautifulSoup

"""CREDABLE

This file is used to determine the reliability index of a news article by comparing it to news articles with existing
reliability indices.

The process will start by building a dataset of articles with pre-defined indices. Then it will take the inputted news
article and compare its contents with related articles and calculate its corresponding reliability index.

"""

"""This section will be used for creating and updating the database of urls."""
WEBSITE_DATABASE = set()


class Website:
    """A class used to define a website.

    Instance Attributed:
        - url: String representation of the url for the website.
        - index: Float value between 0 and 1 representing the reliability index. Default is set to -1 for Website's
        without an index.
        - headline: String representation for the headline of the Website.
        """
    url: str
    headline: str
    site: str
    index: float = -1

    def __init__(self, url: str, headline: str, index: float = -1) -> None:
        self.url = url
        self.headline = headline
        self.index = index


def add_website(article: Website) -> None:
    """This function adds the website to the WEBSITE_DATABASE."""
    WEBSITE_DATABASE.add(article)


def add_websites(articles: set) -> None:
    """This function adds all the urls in urls to URL_DATABASE."""
    for article in articles:
        add_website(article)


"""This section will be used for calculating the reliability index of a url."""


def compare(article1: Website, article2: Website) -> float:
    """This function takes two news articles with urls url1 and url2 and returns a reliability index for url1
    between 0 and 1 by comparing it to the contents of url2 and its given reliability index."""

2
