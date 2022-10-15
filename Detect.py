from GoogleNews import GoogleNews


def detect(url: str) -> bool:
    googlenews = GoogleNews()
    googlenews.search('site:'+url)
    news = googlenews.results()

    if str(news) == '[]':
        return False

    for i in news:
        if i['link'] in url:
            return True
    return False
