from tunepy.interfaces import AbstractOptimizer


class BasicRestartOptimizer(AbstractOptimizer):
    def __init__(self, optimizer_builder, genome_factory, population_size, convergence_criterion):
        self._optimizer_builder = optimizer_builder
        self._genome_factory = genome_factory
        self._population_size = population_size
        self._convergence_criterion = convergence_criterion
        self._max_fitness = float('-inf')
        self._converged = False
        self._best_genome = None

    def next(self):
        new_optimizer = self._optimizer_builder \
            .add_to_initial_population_from_factory(self._genome_factory, self._population_size) \
            .build()

        while not new_optimizer.converged():
            new_optimizer.next()

        self._converged = self._convergence_criterion.converged([self.best_genome], [new_optimizer.best_genome])

        if new_optimizer.best_genome.fitness > self._max_fitness:
            self._max_fitness = new_optimizer.best_genome.fitness
            self._best_genome = new_optimizer.best_genome

    @property
    def converged(self):
        return self._converged

    @property
    def best_genome(self):
        return self._best_genome
