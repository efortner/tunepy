from abc import ABC, abstractmethod


class AbstractConvergenceCriterion(ABC):
    """
    Interface for algorithms that declare convergence of an optimizer.
    """

    @abstractmethod
    def converged(self, old_population, new_population):
        """
        Determines convergence of an optimizer.
        :param old_population: Iterable of Genome objects of the prior generation.
        :param new_population: Iterable of Genomes objects the current generation.
        :return: True if converged, else, False.
        """
        pass
