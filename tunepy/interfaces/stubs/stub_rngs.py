from tunepy.interfaces import AbstractRandomNumberGenerator
import numpy as np


class NumpyOnesRandom(AbstractRandomNumberGenerator):
    """
    Returns a numpy array of ones in whatever shape is provided.
    """

    def random(self):
        return 1.0

    def random_int_array(self, minimum, maximum, shape):
        return np.ones(shape=shape, dtype='int')


class NumpyPassThroughRandom(AbstractRandomNumberGenerator):
    """
    Returns an input passed on instantiation.
    """

    def __init__(self, constant_random):
        self._constant_random = constant_random

    def random_int_array(self, minimum, maximum, shape):
        return self._constant_random * np.ones(shape=shape, dtype='int')

    def random(self):
        return self._constant_random
