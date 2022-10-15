
from newspaper import Article
from flask import Flask


app = Flask(__name__)

@app.route('/')
def summerize(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.summary

if __name__ == "__main__":
    app.run

@app.route('/')
def summerize(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.summary

if __name__ == "__main__":
    app.run