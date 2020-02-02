from tunepy.interfaces import AbstractRandomNumberGenerator
import numpy as np


class ConstantNumpyRandom(AbstractRandomNumberGenerator):
    """
    Returns a numpy array of ones in whatever shape is provided.
    """

    def random_int(self, minimum, maximum):
        return self.random_int_array(minimum, maximum, shape=(1,))[0]

    def random_int_array(self, minimum, maximum, shape):
        return np.ones(shape=shape, dtype='int')
