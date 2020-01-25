from tunepy.interfaces import AbstractRandomNumberGenerator
import numpy as np


class ConstantNumpyRandom(AbstractRandomNumberGenerator):
    """
    Returns a numpy array of ones in whatever shape is provided.
    """

    def random_int(self, minimum, maximum, shape):
        return np.ones(shape=shape, dtype='int')
