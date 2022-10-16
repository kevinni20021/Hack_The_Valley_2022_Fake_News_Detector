from GoogleNews import GoogleNews
import requests
from bs4 import BeautifulSoup


def relatedArticles(url: str) -> any:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    reqs = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    titles = []
    for title in soup.find_all('title'):
        titles.append(title.get_text())
    title = titles[0]
    if titles[0].__contains__('|'):
        title = titles[0].split('|', 1)[0]

    elif titles[0].__contains__('-'):
        title = titles[0].split('-', 1)[0]
    googlenews = GoogleNews()
    googlenews.search(title)
    news = googlenews.results()
    list_of_links = []

    i = 0
    for article in news:
        if article['link'] not in url and i < 3:
            list_of_links.append(article['link'])
            i+=1
    return list_of_links
