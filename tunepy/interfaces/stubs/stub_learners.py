from tunepy.interfaces import AbstractLearner


class ConstantFitnessLearner(AbstractLearner):
    """
    A learner with a fitness defined on construction.
    """

    def __init__(self, fitness):
        self._fitness = fitness

    def fit(self, x, y):
        pass

    def evaluate(self, x):
        return self.fitness

    @property
    def fitness(self):
        return self._fitness
