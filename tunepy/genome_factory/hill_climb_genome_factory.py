from tunepy.interfaces import AbstractGenomeFactory
from tunepy.internal import Genome
import numpy as np


class HillClimberGenomeFactory(AbstractGenomeFactory):
    def __init__(self, dimensions, rng, fitness_func, *args, **kwargs):
        self._dimensions = dimensions
        self._rng = rng
        self._fitness_func = fitness_func
        self._bit_index = 0
        self._args = args
        self._kwargs = kwargs

    def build(self, prior_genomes):
        def bit_flip(bit_value):
            if bit_value == 0:
                return 1
            else:
                return 0

        selected_genome = prior_genomes[self._rng.random_int(0, len(prior_genomes))]
        new_bitstring = np.array(selected_genome.bitstring)
        new_bitstring.ravel()

        self._bit_index %= len(new_bitstring)

        new_bitstring[self._bit_index] = bit_flip(new_bitstring[self._bit_index])
        new_bitstring = new_bitstring.reshape(shape=self._dimensions)

        self._bit_index += 1

        return Genome(self._fitness_func, new_bitstring, *self._args, **self._kwargs)

    @property
    def dimensions(self):
        return self._dimensions
