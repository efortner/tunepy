from tunepy.interfaces import AbstractModelBuilder
from tunepy.interfaces.stubs import ConstantFitnessLearner


class ConstantFitnessLearnerBuilder(AbstractModelBuilder):
    """
    Builds ConstantFitnessLearners.
    """

    def __init__(self, fitness):
        self._fitness = fitness

    def build(self, bitstring):
        return ConstantFitnessLearner(self._fitness)
