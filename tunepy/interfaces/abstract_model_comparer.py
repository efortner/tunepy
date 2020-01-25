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
        :return: Vector containing a filtered list of models.
        """
        pass
