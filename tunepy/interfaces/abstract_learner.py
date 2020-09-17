from abc import ABC, abstractmethod
from typing import Tuple


class AbstractLearner(ABC):
    """
    The common interface that tunepy expects from all machine learning algorithms.
    """

    @abstractmethod
    def fit(self, x_train: Tuple, y_train: Tuple):
        """
        Trains the model on a labeled dataset

        :param x_train: table of features
        :param y_train: vector of labels
        """
        pass

    @abstractmethod
    def evaluate(self, x_test: Tuple, y_test: Tuple) -> float:
        """
        Returns a fitness score after predicting labels on a dataset

        :param x_test: table of features.
        :param y_test: vector of labels for fitness evaluation.
        :return: A fitness score
        """
        pass

    @property
    @abstractmethod
    def fitness(self) -> float:
        """
        The fitness score of this machine learning model

        :return: The fitness score of this machine learning model
        """
        pass
