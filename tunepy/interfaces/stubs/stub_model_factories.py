from tunepy.interfaces import AbstractModelFactory
from tunepy.interfaces.stubs import ConstantFitnessLearner


class ConstantFitnessLearnerFactory(AbstractModelFactory):
    """
    Builds ConstantFitnessLearners.
    """

    @staticmethod
    def generate_bitstring(rng):
        return [0]

    def __init__(self, fitness):
        self._fitness = fitness

    def build(self, bitstring):
        return ConstantFitnessLearner(self._fitness)
