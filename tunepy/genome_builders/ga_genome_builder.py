from tunepy.interfaces import AbstractGenomeBuilder
from tunepy.internal import Genome, DimensionsMismatchException


class UniformCrossoverGenomeBuilder(AbstractGenomeBuilder):
    def __init__(self, dimensions, rng, mutation_rate, comparer, fitness_func, *args, **kwargs):
        self._dimensions = dimensions
        self._rng = rng
        self._mutation_rate = mutation_rate
        self._comparer = comparer
        self._fitness_func = fitness_func
        self._args = args
        self._kwargs = kwargs

    def build(self, prior_genomes):
        def recursive_gene_selection(sub_dimensions, sub_new_bitstring, sub_left_bitstring, sub_right_bitstring):
            if not (sub_dimensions[0] == len(sub_right_bitstring) and
                    sub_dimensions[0] == len(sub_left_bitstring)):
                raise DimensionsMismatchException

            if len(sub_dimensions) == 1:
                for index in range(sub_dimensions[0]):
                    if self._rng.random() > self._mutation_rate:
                        if self._rng.random() < 0.5:
                            sub_new_bitstring[index] = sub_left_bitstring[index]
                        else:
                            sub_new_bitstring[index] = sub_right_bitstring[index]
            else:
                for index in range(sub_dimensions[0]):
                    recursive_gene_selection(
                        sub_dimensions[1:],
                        sub_new_bitstring[index],
                        sub_left_bitstring[index],
                        sub_right_bitstring[index])

        new_bitstring = self._rng.random_int_array(0, 2, self._dimensions)
        left_prior = self._comparer.compare(prior_genomes).bitstring
        right_prior = self._comparer.compare(prior_genomes).bitstring

        recursive_gene_selection(self._dimensions, new_bitstring, left_prior, right_prior)

        return Genome(self._fitness_func, new_bitstring, *self._args, **self._kwargs)

class SinglePointCrossoverGenomeBuilder(AbstractGenomeBuilder):
    def __init__(self, dimensions, rng, mutation_rate, comparer, fitness_func, *args, **kwargs):
        self._dimensions = dimensions
        self._rng = rng
        self._mutation_rate = mutation_rate
        self._comparer = comparer
        self._fitness_func = fitness_func
        self._args = args
        self._kwargs = kwargs

    def build(self, prior_genomes):
        def recursive_gene_selection(sub_dimensions, sub_new_bitstring, sub_left_bitstring, sub_right_bitstring):
            if not (sub_dimensions[0] == len(sub_right_bitstring) and
                    sub_dimensions[0] == len(sub_left_bitstring)):
                raise DimensionsMismatchException

            if len(sub_dimensions) == 1:
                sub_new_bitstring[:crossover_index] = sub_left_bitstring[:crossover_index]
                sub_new_bitstring[crossover_index:] = sub_right_bitstring[crossover_index:]

                for index in range(sub_dimensions[0]):
                    if self._rng.random() < self._mutation_rate:
                        sub_new_bitstring[index] = self._rng.random_int(0, 2)
            else:
                for index in range(sub_dimensions[0]):
                    recursive_gene_selection(
                        sub_dimensions[1:],
                        sub_new_bitstring[index],
                        sub_left_bitstring[index],
                        sub_right_bitstring[index])

        new_bitstring = self._rng.random_int_array(0, 2, self._dimensions)
        left_prior = self._comparer.compare(prior_genomes).bitstring
        right_prior = self._comparer.compare(prior_genomes).bitstring
        crossover_index = self._rng.random_int(1, self._dimensions[-1])

        recursive_gene_selection(self._dimensions, new_bitstring, left_prior, right_prior)

        return Genome(self._fitness_func, new_bitstring, *self._args, **self._kwargs)