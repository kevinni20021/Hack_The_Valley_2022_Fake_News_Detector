import requests
from newspaper import Article
from flask import *
from flask_cors import CORS, cross_origin
from Detect import detect
from Article_scraping import relatedArticles

app = Flask(__name__)
@app.route('/scrape', methods = ['POST', 'GET'])
def summerize():
    if request.method == 'GET':
        return "ok", 200
    if request.method == 'POST':
        url = request.data.decode().split('"',4)[3]\
        if not detect(url):
            return []
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        print(article.summary)
        return article.summary

if __name__ == "__main__":
    app.run(debug = True)
    '''
    #get url
    url = "something"
    if not detect(url):
        pass;
        #send not valid message back to frontend
    else:
        #if real news:
            #send message back thats its real, along with summary, related articles and title
    '''




