from abc import ABC, abstractmethod


class AbstractModelBuilder(ABC):
    """
    The common interface for that tunepy expects from all model builders.
    """

    @abstractmethod
    def build(self, bitstring):
        """
        Builds a new model object with hyperparameters derived from the provided bitstring.
        :param bitstring: A bitstring representing hyperparameters for this model.
        :return: A new, untrained learner.
        """
        pass

    @staticmethod
    @abstractmethod
    def generate_bitstring(rng):
        """
        Generates a new bitstring of the correct dimensions for this model builder.
        :param rng: A random number generator that implements AbstractRandomNumberGenerator.
        :return: A bitstring.
        """
        pass
