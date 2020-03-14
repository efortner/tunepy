from tunepy import InitialPopulationUndefinedException, Genome
from tunepy.interfaces import AbstractOptimizerBuilder
from tunepy.optimizers import BasicOptimizer


class BasicOptimizerBuilder(AbstractOptimizerBuilder):
    def __init__(self, dimensions, fitness_func, new_candidate_genome_factory, convergence_criterion, *args, **kwargs):
        self._dimensions = dimensions
        self._fitness_func = fitness_func
        self._new_candidate_genome_factory = new_candidate_genome_factory
        self._convergence_criterion = convergence_criterion
        self._args = args
        self._kwargs = kwargs
        self._population = []

    def add_to_initial_population_from_factory(self, genome_factory, n):
        base_genome = Genome.new_default_genome(genome_factory.dimensions,
                                                self._fitness_func,
                                                *self._args,
                                                **self._kwargs)
        self._population.append(
            [genome_factory.build([base_genome]) for _ in range(n)]
        )
        return self

    def add_to_initial_population(self, genome):
        self._population.append(genome)
        return self

    def build(self):
        for genome in self._population:
            genome.run()

        if len(self._population) < 1:
            raise InitialPopulationUndefinedException

        new_optimizer = BasicOptimizer(self._population[0],
                                       self._new_candidate_genome_factory,
                                       self._convergence_criterion)

        self._population = []

        return new_optimizer
