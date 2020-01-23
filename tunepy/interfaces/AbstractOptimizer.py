from abc import ABC, abstractmethod


class AbstractOptimizer(ABC):
    """
    The common interface for that tunepy expects from all optimizing algorithms.
    """

    @abstractmethod
    def next(self):
        """
        Performs the next iteration of optimization.

        """
        pass

    @property
    @abstractmethod
    def converged(self):
        """
        Whether or not this algorithm has converged.

        :return: A boolean true when this algorithm has converged or false if not.
        """
        pass
