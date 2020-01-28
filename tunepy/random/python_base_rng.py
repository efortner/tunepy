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
                append_new_random_vector(new_shape[0], array)
            else:
                append_new_list_and_recurse(new_shape, array)

        def append_new_random_vector(length, array):
            for _ in range(length):
                array.append(random.randrange(minimum, maximum))

        def append_new_list_and_recurse(new_shape, array):
            for _ in range(new_shape[0]):
                array.append([])
                traverse_next_dimension(new_shape[1:], array[-1])

        return_array = []
        traverse_next_dimension(shape, return_array)
        return return_array
