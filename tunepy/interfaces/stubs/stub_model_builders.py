from tunepy.interfaces import AbstractModelBuilder
from tunepy.interfaces.stubs import ConstantFitnessLearner


class ConstantFitnessLearnerBuilder(AbstractModelBuilder):
    """
    Builds ConstantFitnessLearners
    """

    def build(self, bitstring):
        return ConstantFitnessLearner()
