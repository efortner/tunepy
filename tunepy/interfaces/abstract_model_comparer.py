from abc import ABC, abstractmethod


class AbstractModelComparer(ABC):
    """
    The common interface for that tunepy expects from all model comparers.
    """

    @abstractmethod
    def compare(self, models):
        """
        Takes a list of models and determines of subset that have the most desirable fitness.

        :param models: Vector of models that implement the AbstractLearningAlgorithm interface.
        :return: A single model that has been determined to be the best.
        """
        pass
