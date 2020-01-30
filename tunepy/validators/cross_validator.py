from tunepy.interfaces import AbstractValidator
from tunepy.internal import *
from copy import deepcopy


class CrossValidator(AbstractValidator):
    """
    Trains a set number of models on subsets of the provided data and returns the average fitness
    of the trained models.
    """

    def __init__(self, bins):
        """
        Creates a new CrossValidator.
        :param bins: The number of bins to divide the data into. Must be at least 2.
        """
        if bins < 2:
            raise CrossValidatorBinException
        self._bins = bins

    def validate(self, x, y, model):
        """
        Creates a holistic fitness score for the provided model and data.
        :param x: Array-like dataset features.
        :param y: Array-like dataset labels.
        :param model: An untrained model of a class than implements AbstractLearner.
        :return:
        """
        if len(x) != len(y):
            raise DataMismatchException

        self._divide_data(x, y)

        total_fitness = 0.0

        for _ in range(self._bins):
            pass


    def _divide_data(self, x, y):
        total_rows = len(y)
        extra_rows = total_rows % self._bins
        bin_size = int((total_rows - extra_rows) / self._bins)

        self._feature_bins_test = [None for _ in range(self._bins)]
        self._label_bins_test = [None for _ in range(self._bins)]

        for index in range(self._bins):
            start_slice = index * bin_size
            end_slice = (index + 1) * bin_size
            if index == self._bins - 1:
                self._feature_bins_test[index] = x[start_slice:]
                self._label_bins_test[index] = y[start_slice:]
            else:
                self._feature_bins_test[index] = x[start_slice:end_slice]
                self._label_bins_test[index] = y[start_slice:end_slice]
