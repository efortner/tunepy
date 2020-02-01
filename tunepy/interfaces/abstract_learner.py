from abc import ABC, abstractmethod


class AbstractLearner(ABC):
    """
    The common interface for that tunepy expects from all machine learning algorithms.
    """

    @abstractmethod
    def fit(self, x_train, y_train):
        """
        Trains the model on a labeled dataset.

        :param x_train: Array-like table of features.
        :param y_train: Vector of labels.
        """
        pass

    @abstractmethod
    def evaluate(self, x_test, y_test):
        """
        Returns a fitness score after predicting labels on a dataset. Higher fitness
        scores indicate better performance.

        :param x_test: Array-like table of features.
        :param y_test: Array-like vector of labels for fitness evaluation.
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
