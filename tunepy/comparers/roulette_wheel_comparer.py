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
        self._max_fitness = 0.0

    def compare(self, models):
        """
        Returns one model for the provided list of models chosen by roulette wheel style selection.
        :param models: Array-like of objects implementing AbstractLearner.
        :return: One model object from models.
        """

        self._extract_fitness_from_models(models)

        while True:
            chosen_model = models[self._rng.random_int(0, len(models))]
            acceptance_probability = chosen_model.fitness / self._max_fitness
            if acceptance_probability > self._rng.random():
                return chosen_model

    def _extract_fitness_from_models(self, models):
        new_hash_models = hash(tuple(models))
        if new_hash_models == self._hash_models:
            return False

        self._hash_models = new_hash_models
        self._all_fitness = np.zeros(shape=(len(models),))

        for index in range(len(models)):
            self._all_fitness[index] = models[index].fitness

        self._max_fitness = np.max(self._all_fitness)
        return True
