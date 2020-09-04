from tunepy.interfaces import AbstractLearnerFactory
from tunepy.interfaces.stubs import ConstantFitnessLearner


class ConstantFitnessLearnerFactory(AbstractLearnerFactory):
    """
    Builds ConstantFitnessLearners.
    """

    def __init__(self, fitness):
        self._fitness = fitness

    def build(self, bitstring):
        return ConstantFitnessLearner(self._fitness)
