from tunepy.interfaces import AbstractOptimizer
from tunepy.internal import Genome


class GeneticOptimizer(AbstractOptimizer):
    """
    Optimizes fitness using successive refinements of a population of solutions.
    """

    def __init__(self, x, y, rng, model_builder, validator, population, mutation_rate, minimum_generations):
        self._x = x
        self._y = y
        self._mutation_rate = mutation_rate
        self._rng = rng
        self._model_builder = model_builder
        self._validator = validator
        self._minimum_generations = minimum_generations
        self._population = [self._build_random_genome() for _ in range(population)]

    def next(self):
        pass

    @property
    def converged(self):
        pass

    @property
    def best_genome(self):
        pass

    def _build_random_genome(self):
        bitstring = self._model_builder.generate_bitstring(self._rng)
        return Genome(self._fitness_func, bitstring)

    def _fitness_func(self, bitstring):
        return self._validator.validate(self._x, self._y, self._model_builder.build(bitstring))
