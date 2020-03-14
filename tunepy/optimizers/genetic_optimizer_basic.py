from tunepy.interfaces import AbstractOptimizer
from tunepy.internal import Genome


class BasicGeneticOptimizer(AbstractOptimizer):
    """
    Optimizes fitness using successive refinements of a random population of solutions.
    """

    def __init__(self, initial_population, genome_factory, convergence_criterion):
        self._population = initial_population
        self._genome_factory = genome_factory
        self._convergence_criterion = convergence_criterion
        self._max_fitness = float('-inf')
        self._best_genome = Genome(lambda bitstring: self._best_genome, [])
        self._converged = False

    def next(self):
        old_population = self._population
        self._population = []

        for index in range(len(old_population)):
            new_genome = self._genome_factory.build(old_population)
            self._population.append(new_genome)
            new_genome.run()
            if new_genome.fitness > self._max_fitness:
                self._best_genome = new_genome
                self._max_fitness = self._best_genome.fitness

        self._converged = self._convergence_criterion.converged(old_population, self._population)

    @property
    def converged(self):
        return self._converged

    @property
    def best_genome(self):
        return self._best_genome
