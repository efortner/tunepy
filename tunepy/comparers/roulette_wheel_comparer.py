from tunepy.interfaces import AbstractModelComparer
import numpy as np


class RouletteWheelComparer(AbstractModelComparer):
    """
    Performs a fitness proportionate random model selection. The underlying implementation uses the stochastic
    acceptance method for producing a result in nearly constant time. This is a common method for selecting
    breeding pairs for a genetic algorithm.
    """

    def __init__(self, random_number_generator):
        """
        Creates a new RouletteWheelComparer.
        :param random_number_generator: An object of a class that implements AbstractRandomNumberGenerator.
        """
        self._rng = random_number_generator
        self._hash_models = 0
        self._all_fitness = None
        self._max_fitness = -float('inf')

    def compare(self, genomes):
        """
        Returns one model for the provided list of models chosen by roulette wheel style selection.
        :param genomes: Array-like of genomes.
        :return: One model object from models.
        """

        self.extract_fitness_from_genomes(genomes)

        while True:
            chosen_genome = genomes[self._rng.random_int(0, len(genomes))]
            acceptance_probability = chosen_genome.fitness / self._max_fitness
            if acceptance_probability > self._rng.random():
                return chosen_genome

    def extract_fitness_from_genomes(self, genomes):
        """
        Iterates over all provided genomes and caches their fitness values. This operation is skipped if the
        provided genomes have already been cached.
        :param genomes: Iterable of genomes.
        :return: True if this set of genomes needed to be cached. Else, false.
        """
        new_hash_models = hash(tuple(genomes))
        if new_hash_models == self._hash_models:
            return False

        self._hash_models = new_hash_models
        self._all_fitness = np.zeros(shape=(len(genomes),))

        for index in range(len(genomes)):
            self._all_fitness[index] = genomes[index].fitness

        self._max_fitness = np.max(self._all_fitness)
        return True
