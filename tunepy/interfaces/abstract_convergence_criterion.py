from abc import ABC, abstractmethod


class AbstractConvergenceCriterion(ABC):
    """
    Interface for algorithms that declare convergence of an optimizer.
    """

    @abstractmethod
    def converged(self, old_candidate, new_candidate):
        pass


class AbstractAnnealingSchedule(AbstractConvergenceCriterion):
    @property
    @abstractmethod
    def temperature(self):
        pass
