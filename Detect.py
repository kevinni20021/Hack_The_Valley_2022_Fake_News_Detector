from urllib.request import urlopen

from bs4 import BeautifulSoup
from GoogleNews import GoogleNews


def detect(url: str) -> bool:
    googlenews = GoogleNews()
    googlenews.search('site:' + url)
    news = googlenews.results()

    if str(news) == '[]':
        return False

    for i in news:
        if i['link'] in url:
            return True
    return False


def extractText(url: str) -> str:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines() if len(line.strip())>20)
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text
