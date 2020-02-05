from abc import ABC, abstractmethod


class AbstractModelComparer(ABC):
    """
    The common interface for that tunepy expects from all model comparers.
    """

    @abstractmethod
    def compare(self, genomes):
        """
        Takes a list of models and determines of subset that have the most desirable fitness.

        :param genomes: Vector of Genomes to compare. Assumes all genomes have valid fitness scores.
        :return: A single model that has been determined to be the best.
        """
        pass
