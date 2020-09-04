from abc import ABC, abstractmethod


class AbstractValidator(ABC):
    """
    The common interface tunepy expects from all validators.
    """

    @abstractmethod
    def validate(self, x, y, model):
        """
        Creates a holistic fitness score for the provided model and data.
        :param x: Array-like dataset features.
        :param y: Array-like dataset labels.
        :param model: An untrained model of a class than implements AbstractLearner.
        :return: A fitness score.
        """
        pass
