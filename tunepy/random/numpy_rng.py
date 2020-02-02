from tunepy.interfaces import AbstractRandomNumberGenerator
import numpy as np


class NumpyRNG(AbstractRandomNumberGenerator):
    """
    A tunepy wrapper for the number random number generator.
    """

    def random(self):
        """
        Returns a random number between 0 and 1.
        :return: A single random number between 0 and 1.
        """
        return np.random.random()

    def __init__(self, seed):
        np.random.seed(seed)

    def random_int_array(self, minimum, maximum, shape):
        """
        Builds an array-like structure of random integers.
        :param minimum: Minimum integer value (inclusive).
        :param maximum: Maximum integer value (exclusive).
        :param shape: Tuple representing the shape of the output.
        :return: Array-like collection of integers.
        """
        return np.random.randint(minimum, maximum, size=shape)
