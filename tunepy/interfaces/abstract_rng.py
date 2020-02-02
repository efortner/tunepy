from abc import ABC, abstractmethod


class AbstractRandomNumberGenerator(ABC):
    """
    The common interface for that tunepy expects from all random number generators.
    """

    @abstractmethod
    def random_int_array(self, minimum, maximum, shape):
        """
        Builds an array-like structure of random integers.
        :param minimum: Minimum integer value (inclusive).
        :param maximum: Maximum integer value (exclusive).
        :param shape: Tuple representing the shape of the output.
        :return: Array-like collection of integers.
        """
        pass

    def random_int(self, minimum, maximum):
        """
        Returns a single random integer.
        :param minimum: Minimum integer value (inclusive).
        :param maximum: Maximum integer value (exclusive).
        :return: A random integer.
        """
        return self.random_int_array(minimum, maximum, shape=(1,))[0]