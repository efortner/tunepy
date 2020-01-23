from abc import ABC, abstractmethod


class AbstractLearningAlgorithm(ABC):
    """
    The common interface for that tunepy expects from all machine learning algorithms.
    """

    @abstractmethod
    def fit(self, x, y):
        """
        Trains the model on a labeled dataset.

        :param x: Array-like table of features.
        :param y: Vector of labels.
        """
        pass

    @abstractmethod
    def evaluate(self, x):
        """
        Returns a fitness score after predicting labels on a dataset. Higher fitness
        scores indicate better performance.

        :param x: Array-like table of features.
        :return: A fitness score.
        """
        pass

    @property
    @abstractmethod
    def fitness(self):
        """
        The fitness score of this machine learning model after training using 'evaluate'.

        :return: The fitness score of this machine learning model.
        """
