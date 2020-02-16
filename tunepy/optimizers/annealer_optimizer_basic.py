from tunepy.interfaces import AbstractOptimizer
from math import exp


class BasicAnnealingOptimizer(AbstractOptimizer):
    """
    Performs a randomized optimization of by simulated annealing.
    """

    def __init__(self, initial_candidate, genome_builder, convergence_criterion, rng,
                 initial_temperature=1.0, temperature_decay=0.99):
        self._candidate = initial_candidate
        self._genome_builder = genome_builder
        self._convergence_criterion = convergence_criterion
        self._rng = rng
        self._temperature = initial_temperature
        self._temperature_decay = temperature_decay
        self._max_fitness = float('-inf')
        self._best_genome = None
        self._converged = False

    def next(self):
        old_candidate = self._candidate
        new_candidate = self._genome_builder([old_candidate])
        new_candidate.run()

        if new_candidate.fitness > old_candidate.fitness:
            self._candidate = new_candidate
        else:
            acceptance_probability = exp((new_candidate.fitness - old_candidate.fitness) / self._temperature)
            if self._rng.random() < acceptance_probability:
                self._candidate = new_candidate

        if self._candidate.fitness > self._max_fitness:
            self._best_genome = self._candidate
            self._max_fitness = self._candidate.fitness

        self._temperature *= self._temperature_decay
        self._converged = self._convergence_criterion([old_candidate], [self._candidate])

    @property
    def converged(self):
        return self._converged

    @property
    def best_genome(self):
        return self._best_genome
