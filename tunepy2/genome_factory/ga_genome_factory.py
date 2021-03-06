from typing import Callable, List, Dict, Tuple

from tunepy2.interfaces import AbstractGenomeFactory, AbstractRandomNumberGenerator, AbstractGenomeComparer
from tunepy2.internal import Genome, DimensionsMismatchException


class UniformCrossoverGenomeFactory(AbstractGenomeFactory):
    """ Genome factory that allows crossover of bits from either parent """

    def __init__(self,
                 dimensions: Tuple,
                 rng: AbstractRandomNumberGenerator,
                 mutation_rate: float,
                 comparer: AbstractGenomeComparer,
                 fitness_func: Callable[..., float],
                 *args,
                 **kwargs):
        """ Creates a new UniformCrossoverGenomeFactory

        :param dimensions: dimensions of bitstrings of Genome objects generated by the factory
        :param rng: random number generator
        :param mutation_rate: probability of mutation (must be (0.0, 1.0))
        :param comparer: comparer used to select Genome objects
        :param fitness_func: fitness function passed into new Genome objects that accepts a bitstring
        :param args: will be passed into fitness_func
        :param kwargs: will be passed into fitness_func
        """
        self._dimensions = dimensions
        self._rng = rng
        self._mutation_rate = mutation_rate
        self._comparer = comparer
        self._fitness_func = fitness_func
        self._args = args
        self._kwargs = kwargs

    def build(self, prior_genomes: List[Genome]) -> Genome:
        """ Builds a new Genome from a list of priors

        :param prior_genomes: list of prior Genomes
        :return: a new Genome object
        """
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

    @property
    def dimensions(self) -> Tuple:
        """

        :return: the dimensions of Genome objects returned by this factory
        """
        return self._dimensions


class SinglePointCrossoverGenomeFactory(AbstractGenomeFactory):
    """ Genome factory that takes all bits prior to a crossover point from one parent and all bits after and
    including a crossover point from the other parent """

    def __init__(self,
                 dimensions: Tuple,
                 rng: AbstractRandomNumberGenerator,
                 mutation_rate: float,
                 comparer: AbstractGenomeComparer,
                 fitness_func: Callable[..., float],
                 *args,
                 **kwargs):
        """ Creates a new SinglePointCrossoverGenomeFactory

        :param dimensions: dimensions of bitstrings of Genome objects generated by the factory
        :param rng: random number generator
        :param mutation_rate: probability of mutation (must be (0.0, 1.0))
        :param comparer: comparer used to select Genome objects
        :param fitness_func: fitness function passed into new Genome objects that accepts a bitstring
        :param args: will be passed into fitness_func
        :param kwargs: will be passed into fitness_func
        """
        self._dimensions = dimensions
        self._rng = rng
        self._mutation_rate = mutation_rate
        self._comparer = comparer
        self._fitness_func = fitness_func
        self._args = args
        self._kwargs = kwargs

    def build(self, prior_genomes: List[Genome]) -> Genome:
        """ Builds a new Genome from a list of priors

        :param prior_genomes: list of prior Genomes
        :return: a new Genome object
        """
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

    @property
    def dimensions(self) -> Tuple:
        """

        :return: the dimensions of Genome objects returned by this factory
        """
        return self._dimensions
