import ReliabilityCalculator2

if __name__ == "__main__":
    train_set = ReliabilityCalculator2.extract_train_set("news.csv", "text")
    pac, tfidf = ReliabilityCalculator2.train_model(train_set[0], train_set[1])
    text = "Hillary Clinton has awkwardly wound her way through numerous scandals in just this " \
           "election cycle. But she’s never shown fear or desperation before. Now that has changed." \
           " Whatever she is afraid of, it lies buried in her emails with Huma Abedin. And it can " \
           "bring her down like nothing else has.  "
    score = ReliabilityCalculator2.test_text(text, pac, tfidf)
    print(score)
