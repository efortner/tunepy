from tunepy.interfaces import AbstractValidator
from tunepy.internal import DimensionsMismatchException, TrainTestSplitException


class TrainTestValidator(AbstractValidator):
    def __init__(self, train_test_ratio):
        self._train_test_ratio = train_test_ratio
        self._x = []
        self._y = []
        self._test_features = []
        self._test_labels = []
        self._train_features = []
        self._train_labels = []

    def validate(self, x, y, model):
        if len(x) != len(y):
            raise DimensionsMismatchException

        self.split_data(x, y)
        model.fit(self.training_data_features, self.training_data_labels)
        return float(model.evaluate(self.test_data_features, self.training_data_labels))

    def split_data(self, x, y):
        if len(x) != len(y):
            raise DimensionsMismatchException

        self._x = x
        self._y = y

        size_train = int(self._train_test_ratio * len(x))

        if size_train <= 0 or size_train >= len(x):
            raise TrainTestSplitException

        self._train_features = self._x[:size_train]
        self._train_labels = self._y[:size_train]
        self._test_features = self._x[size_train:]
        self._test_labels = self._y[size_train:]

    @property
    def test_data_features(self):
        return self._test_features

    @property
    def test_data_labels(self):
        return self._test_labels

    @property
    def training_data_features(self):
        return self._train_features

    @property
    def training_data_labels(self):
        return self._train_labels
