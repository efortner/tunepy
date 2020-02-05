

class Genome(object):
    """
    Represents a single genome.
    """

    def __init__(self, fitness_func, bitstring, *args, **kwargs):
        """
        Creates a new genome.
        :param fitness_func: A function that returns the fitness of this genome.
        :param bitstring: Will be passed into the fitness function.
        :param args: Will be passed into the fitness function.
        :param kwargs: Will be passed into the fitness function.
        """
        self._fitness_func = fitness_func
        self._bitstring = bitstring
        self._args = args
        self._kwargs = kwargs
        self._fitness = float("-inf")

    def run(self):
        self._fitness = self._fitness_func(self._bitstring, *self._args, **self._kwargs)

    @property
    def bitstring(self):
        return self._bitstring

    @property
    def fitness(self):
        return self._fitness
