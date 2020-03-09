from tunepy.interfaces import AbstractOptimizer
from copy import deepcopy


class BasicRandomRestartOptimizer(AbstractOptimizer):
    def __init__(self, genome_builder, convergence_criterion):
        self._genome_builder = genome_builder
        self._convergence_criterion = convergence_criterion
        self._max_fitness = float('-inf')
        self._converged = False
        self._best_genome = None

    def next(self):
        pass

    @property
    def converged(self):
        return self._converged

    @property
    def best_genome(self):
        return self._best_genome
