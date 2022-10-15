from newspaper import Article

def summerize(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.summary

a = "https://www.cbc.ca/news/health/covid19-pandemic-emergency-over-omicron-1.6616471"
if True:
    print(summerize(a))