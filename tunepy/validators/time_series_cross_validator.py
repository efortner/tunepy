from copy import deepcopy

from tunepy import DimensionsMismatchException, TimeSeriesCrossValidatorBinException
from tunepy.interfaces import AbstractValidator


class TimeSeriesCrossValidator(AbstractValidator):
    def __init__(self, bins):
        self._bins = bins
        self._feature_bins = []
        self._label_bins = []

    def validate(self, x, y, model):
        if self._bins < 2:
            raise TimeSeriesCrossValidatorBinException

        if len(x) != len(y):
            raise DimensionsMismatchException

        self.build_bins(x, y)

        total_fitness = 0.0

        for index in range(self._bins - 1):
            model_copy = deepcopy(model)
            model_copy.fit(self._feature_bins[index], self._label_bins[index])
            model_copy.evaluate(self._feature_bins[index+1], self._label_bins[index+1])
            total_fitness += model_copy.fitness

        return total_fitness / (self._bins - 1)

    def build_bins(self, x, y):
        if len(x) != len(y):
            raise DimensionsMismatchException

        total_rows = len(y)
        extra_rows = total_rows % self._bins
        bin_size = int((total_rows - extra_rows) / self._bins)

        self._feature_bins = [None for _ in range(self._bins)]
        self._label_bins = [None for _ in range(self._bins)]

        for index in range(self._bins):
            start_slice = index * bin_size
            end_slice = (index + 1) * bin_size
            if index == self._bins - 1:
                self._feature_bins[index] = x[start_slice:]
                self._label_bins[index] = y[start_slice:]
            else:
                self._feature_bins[index] = x[start_slice:end_slice]
                self._label_bins[index] = y[start_slice:end_slice]

    @property
    def bins(self):
        return self._bins

    @property
    def feature_bins(self):
        return self._feature_bins

    @property
    def label_bins(self):
        return self._label_bins
