from typing import Any

import pandas as pd

import sklearn.model_selection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

"""MAKE THE WORLD HONEST AGAIN"""


def extract_train_set(filename: str, data: str) -> tuple[Any, Any]:
    df = pd.read_csv(filename)
    labels = df.label
    x_train, _, y_train, _ = \
        sklearn.model_selection.train_test_split(df[data], labels, train_size=0.99, random_state=7)
    return x_train, y_train


def train_model(train_set: object, train_results: object) -> tuple[PassiveAggressiveClassifier, TfidfVectorizer]:
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    tfidf_train = tfidf_vectorizer.fit_transform(train_set)
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(tfidf_train, train_results)
    return pac, tfidf_vectorizer


def test_text(text: str, pac: PassiveAggressiveClassifier, tfidf: TfidfVectorizer) -> str:
    tfidf_test = tfidf.transform([text])
    y_pred = pac.predict(tfidf_test)
    return y_pred
