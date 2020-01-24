from tunepy.interfaces import AbstractRandomNumberGenerator
import numpy as np


class ConstantNumpyRandom(AbstractRandomNumberGenerator):
    """
    Returns a numpy array of ones in whatever shape is provided.
    """
    def __init__(self, seed):
        super().__init__(seed)

    def random_int(self, minimum, maximum, shape):
        return np.ones(shape=shape, dtype='int')
