from classifier import Classify
from news_scraper import scraper
from sklearn.model_selection import train_test_split


class predict1():

    def __init__(self, keyword):
        self.score = 0
        self.articles = 0
        self.keyword = keyword
        self.predictor()

    def predictor(self):
        sc = scraper(self.keyword).results
        self.articles = len(sc)

        for i in sc:
            value = Classify(i["title"]).classify()
            self.score+=value

        self.final_pred = self.score/self.articles
