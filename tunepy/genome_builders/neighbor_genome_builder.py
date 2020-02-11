from tunepy.interfaces import AbstractGenomeBuilder
from tunepy.internal import Genome
from copy import deepcopy


class RandomNeighborGenomeBuilder(AbstractGenomeBuilder):
    def __init__(self, dimensions, rng, fitness_func, n=1, *args, **kwargs):
        self._n = n
        self._dimensions = dimensions
        self._rng = rng
        self._fitness_func = fitness_func
        self._args = args
        self._kwargs = kwargs

    def build(self, prior_genomes):
        def bit_flip(bit_value):
            if bit_value == 0:
                return 1
            else:
                return 0

        def recursive_bit_flip(bitstring, dimensions):
            random_index = self._rng.random_int(0, dimensions[0])
            if len(dimensions) == 1:
                bitstring[random_index] = bit_flip(bitstring[random_index])
            else:
                recursive_bit_flip(bitstring[random_index], dimensions[1:])

        selected_genome = prior_genomes[self._rng.random_int(0, len(prior_genomes))]
        candidate_genome_bitstring = deepcopy(selected_genome.bitstring)

        for _ in range(self._n):
            recursive_bit_flip(candidate_genome_bitstring, self._dimensions)

        return Genome(self._fitness_func, candidate_genome_bitstring, *self._args, **self._kwargs)
