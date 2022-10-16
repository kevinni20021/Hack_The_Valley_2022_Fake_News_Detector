import requests
from newspaper import Article
from flask import *
from flask_cors import CORS, cross_origin
from Detect import detect, extractText
from Article_scraping import relatedArticles
import ReliabilityCalculator2

TRAIN_SET = ReliabilityCalculator2.extract_train_set("news.csv", "text")
PAC, TFIDF = ReliabilityCalculator2.train_model(TRAIN_SET[0], TRAIN_SET[1])
app = Flask(__name__)

@app.route('/scrape', methods = ['POST', 'GET'])
def summerize():
    if request.method == 'GET':
        return "ok", 200
    if request.method == 'POST':
        url = request.data.decode().split('"',4)[3]
        if not detect(url):
            return jsonify(title="Not found", summary="Not found", score="Not found", related1="Not found",
                           related2="Not found", related3="Not found")
        else:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            text = article.text
            score = ReliabilityCalculator2.test_text(text, PAC, TFIDF)
            related = relatedArticles(url)
            if len(related) == 0:
                return jsonify(title=article.title, summary=article.summary, score=score[0], related1="Not found",
                               related2="Not found", related3="Not found")
            elif len(related) == 1:
                return jsonify(title=article.title, summary=article.summary, score=score[0], related1=related[0],
                               related2="Not found", related3="Not found")
            elif len(related) == 2:
                return jsonify(title = article.title, summary = article.summary, score = score[0], related1 = related[0],
                        related2 = related[1], related3 = "Not found")
            else:
                return jsonify(title = article.title, summary = article.summary, score = score[0], related1 = related[0],
                        related2 = related[1], related3 = related[2])

if __name__ == "__main__":
    app.run(debug = True)
    '''
    pseudo code lol
    #get url
    url = "something"
    if not detect(url):
        pass;
        #send not valid message back to frontend
    else:
        #if real news:
            #send message back thats its real, along with summary, related articles and title
    '''

