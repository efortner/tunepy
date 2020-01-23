from abc import ABC, abstractmethod


class AbstractRandomNumberGenerator(ABC):
    """
    The common interface for that tunepy expects from all random number generators.
    """

    @abstractmethod
    def __init__(self, seed):
        """
        Creates a new random number generator.
        :param seed: The seed that will be used for this random number generator.
        """
        self.seed = seed
        super().__init__()

    @abstractmethod
    def random_int(self, minimum, maximum, shape):
        """
        Builds an array-like structure of random integers.
        :param minimum: Minimum integer value (inclusive).
        :param maximum: Maximum integer value (exclusive).
        :param shape: Tuple representing the shape of the output.
        :return: Array-like collection of integers.
        """
        pass
