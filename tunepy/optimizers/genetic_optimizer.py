from tunepy.interfaces import AbstractOptimizer
from tunepy.internal import Genome


class GeneticOptimizer(AbstractOptimizer):
    """
    Optimizes fitness using successive refinements of a population of solutions.
    """

    def __init__(self, initial_population, genome_builder, minimum_generations):
        self._genome_builder = genome_builder
        self._population = initial_population
        self._minimum_generations = minimum_generations

    def next(self):
        pass

    @property
    def converged(self):
        pass

    @property
    def best_genome(self):
        pass
