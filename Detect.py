from GoogleNews import GoogleNews



def detect(URL: str) -> bool:
    googlenews = GoogleNews()
    googlenews.search(URL)
    news = googlenews.results()

    if str(news) == '[]':
        return False

    for i in news:
        if i['link'] == URL:
            return True
    return False
