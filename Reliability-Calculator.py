import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

"""MAKE THE WORLD HONEST AGAIN

This file is used to determine the reliability index of a news article by comparing it to news articles with existing
reliability indices.

The process will start by building a dataset of articles with pre-defined indices. Then it will take the inputted news
article and compare its contents with related articles and calculate its corresponding reliability index.

"""

"""This section will be used for creating and updating the database of urls."""
URL_DATABASE = {}

if __name__ == "__main__":
    # Read the data
    df = pd.read_csv('news.csv')
    # DataFlair - Get the labels
    labels = df.label
    # DataFlair - Split the dataset
    x_train, x_test, y_train, y_test = train_test_split(df['text'], labels, test_size=0.2, random_state=7)
    # DataFlair - Initialize a TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    # DataFlair - Fit and transform train set, transform test set
    tfidf_train = tfidf_vectorizer.fit_transform(x_train)
    tfidf_test = tfidf_vectorizer.transform(x_test)
    # DataFlair - Initialize a PassiveAggressiveClassifier
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(tfidf_train, y_train)

    # DataFlair - Predict on the test set and calculate accuracy
    y_pred = pac.predict(tfidf_test)
    score = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {round(score * 100, 2)}%')
    # DataFlair - Build confusion matrix
    confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])


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
