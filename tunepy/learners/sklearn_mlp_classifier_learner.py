from tunepy.interfaces import AbstractLearner
from sklearn.neural_network import MLPClassifier


class SklearnMlpClassifierLearner(AbstractLearner):
    def __init__(self, *args, **kwargs):
        self._learner = MLPClassifier(*args, **kwargs)
        self._fitness = float("-inf")

    def fit(self, x_train, y_train):
        self._learner.fit(x_train, y_train)

    def evaluate(self, x_test, y_test):
        self._fitness = self._learner.score(x_test, y_test)

    @property
    def fitness(self):
        return self._fitness
