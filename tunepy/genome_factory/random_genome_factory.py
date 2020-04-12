from tunepy import Genome
from tunepy.interfaces import AbstractGenomeFactory


class RandomGenomeFactory(AbstractGenomeFactory):
    def __init__(self, dimensions, rng, fitness_func, *args, **kwargs):
        self._rng = rng
        self._dimensions = dimensions
        self._fitness_func = fitness_func
        self._args = args
        self._kwargs = kwargs

    def build(self, prior_genomes):
        bitstring = self._rng.random_int_array(0, 1, self._dimensions)
        return Genome(self._fitness_func, bitstring, *self._args, **self._kwargs)

    @property
    def dimensions(self):
        return self._dimensions
