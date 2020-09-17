from abc import ABC, abstractmethod
from typing import Tuple

from tunepy.interfaces import AbstractLearner


class AbstractValidator(ABC):
    """
    The common interface tunepy expects from all validators.
    """

    @abstractmethod
    def validate(self, x: Tuple, y: Tuple, model: AbstractLearner) -> float:
        """
        Creates a fitness score for the provided model and data

        :param x: array-like dataset features
        :param y: array-like dataset labels
        :param model: untrained learner
        :return: a fitness score
        """
        pass
