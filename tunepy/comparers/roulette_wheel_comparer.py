from tunepy.interfaces import AbstractModelComparer
import numpy as np


class RouletteWheelComparer(AbstractModelComparer):
    """
    Performs a fitness proportionate random model selection. This is a common method for selecting breeding pairs
    for a genetic algorithm.
    """

    def __init__(self, random_number_generator):
        """
        Creates a new RouletteWheelComparer.
        :param random_number_generator:
        """
        self._rng = random_number_generator
        self._hash_models = 0
        self._all_fitness = None
        self._max_fitness = 0.0
        self._fitness_to_model = {}

    def compare(self, models):
        """
        Returns one model for the provided list of models chosen by roulette wheel style selection.
        :param models: Array-like of objects implementing AbstractLearner.
        :return: One model object from models.
        """

        def recursive_fitness_search(all_fitnesses, search_fitness):
            if len(all_fitnesses) == 1:
                return all_fitnesses[0]

            middle_index = int(len(all_fitnesses) / 2)
            if all_fitnesses[middle_index] > search_fitness:
                return recursive_fitness_search(all_fitnesses[:middle_index], search_fitness)
            else:
                return recursive_fitness_search(all_fitnesses[middle_index:], search_fitness)

        self._extract_fitness_from_models(models)
        target_fitness = self._rng.random() * self._max_fitness
        found_fitness = recursive_fitness_search(self._all_fitness, target_fitness)

        return self._fitness_to_model[float(found_fitness)]

    def _extract_fitness_from_models(self, models):
        new_hash_models = hash(tuple(models))
        if new_hash_models == self._hash_models:
            return False

        self._hash_models = new_hash_models
        self._all_fitness = np.zeros(shape=(len(models),))

        for index in range(len(models)):
            current_fitness = float(models[index].fitness)
            self._all_fitness[index] = current_fitness
            self._fitness_to_model[current_fitness] = models[index]

        self._all_fitness = np.sort(self._all_fitness)
        self._max_fitness = np.max(self._all_fitness)
        return True
