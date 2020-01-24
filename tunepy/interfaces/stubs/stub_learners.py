from tunepy.interfaces import AbstractLearner


class ConstantFitnessLearner(AbstractLearner):
    """
    A learner with a fitness of 0.0.
    """

    def fit(self, x, y):
        pass

    def evaluate(self, x):
        return self.fitness

    @property
    def fitness(self):
        return 0.0
