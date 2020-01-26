from tunepy.interfaces import AbstractRandomNumberGenerator
import random


class PythonBaseRNG(AbstractRandomNumberGenerator):
    """
    A tunepy wrapper of the built in Python random number generator.
    """

    def __init__(self, seed):
        random.seed(seed)

    def random_int(self, minimum, maximum, shape):
        """
        Builds an array-like structure of random integers.
        :param minimum: Minimum integer value (inclusive).
        :param maximum: Maximum integer value (exclusive).
        :param shape: Tuple representing the shape of the output.
        :return: Array-like collection of integers.
        """

        def traverse_next_dimension(new_shape, array):
            if len(new_shape) == 1:
                array.append(build_base_case_array(new_shape[0]))
            else:
                array.append(traverse_next_dimension(new_shape[1:], array))
            return array

        def build_base_case_array(length):
            return [random.randrange(minimum, maximum) for _ in range(length)]

        return traverse_next_dimension(shape, [])
