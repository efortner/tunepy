import unittest
from tunepy.validators import CrossValidator
from tunepy.internal import *
from tunepy.interfaces.stubs import *


class TestCrossValidator(unittest.TestCase):
    def test_bin_creation_error(self):
        with self.assertRaises(CrossValidatorBinException):
            CrossValidator(1)

    def test_data_mismatch_error(self):
        data_features = \
            [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2],
             [3, 3, 3, 3, 3],
             [4, 4, 4, 4, 4],
             [5, 5, 5, 5, 5]]

        data_labels = \
            [0, 1, 2, 3, 4]

        validator = CrossValidator(5)

        with self.assertRaises(DataMismatchException):
            validator.validate(data_features, data_labels, None)

    def test_evaluation_bin_sizes(self):
        data_features = \
            [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2],
             [3, 3, 3, 3, 3],
             [4, 4, 4, 4, 4],
             [5, 5, 5, 5, 5]]

        data_labels = \
            [0, 1, 2, 3, 4, 5]

        validator = CrossValidator(5)
        validator.build_test_bins(data_features, data_labels)

        self.assertEqual(5, len(validator.test_data_features))
        self.assertEqual(5, len(validator.test_data_labels))

        self.assertEqual(1, len(validator.test_data_features[0]))
        self.assertEqual(1, len(validator.test_data_labels[0]))

        self.assertEqual(2, len(validator.test_data_features[-1]))
        self.assertEqual(2, len(validator.test_data_labels[-1]))

    def test_train_bin_sizes(self):
        data_features = \
            [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2],
             [3, 3, 3, 3, 3],
             [4, 4, 4, 4, 4],
             [5, 5, 5, 5, 5]]

        data_labels = \
            [0, 1, 2, 3, 4, 5]

        validator = CrossValidator(5)
        validator.build_train_bins(data_features, data_labels)

        self.assertEqual(5, len(validator.training_data_features))
        self.assertEqual(5, len(validator.training_data_labels))

        self.assertEqual(5, len(validator.training_data_features[0]))
        self.assertEqual(5, len(validator.training_data_labels[0]))

        self.assertEqual(4, len(validator.training_data_features[-1]))
        self.assertEqual(4, len(validator.training_data_labels[-1]))

    def test_validation_result(self):
        data_features = \
            [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2],
             [3, 3, 3, 3, 3],
             [4, 4, 4, 4, 4]]

        data_labels = \
            [0, 1, 2, 3, 4]

        validator = CrossValidator(5)
        fitness = validator.validate(data_features, data_labels, ConstantFitnessLearner(69.0))
        self.assertAlmostEqual(69.0, fitness)


if __name__ == '__main__':
    unittest.main()
