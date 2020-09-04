from abc import ABC, abstractmethod


class AbstractLearnerFactory(ABC):
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
