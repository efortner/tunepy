from tunepy import Genome, InitialPopulationUndefinedException
from tunepy.interfaces import AbstractOptimizerBuilder
from tunepy.optimizers import BasicAnnealingOptimizer


class BasicAnnealerOptimizerBuilder(AbstractOptimizerBuilder):
    def __init__(self,
                 dimensions,
                 rng,
                 new_candidate_genome_factory,
                 annealing_schedule,
                 fitness_func,
                 *args,
                 **kwargs):
        self._dimensions = dimensions
        self._rng = rng
        self._fitness_func = fitness_func
        self._new_candidate_genome_factory = new_candidate_genome_factory
        self._annealing_schedule = annealing_schedule
        self._args = args
        self._kwargs = kwargs
        self._population = []

    def add_to_initial_population_from_factory(self, genome_factory, n):
        base_genome = Genome.new_default_genome(genome_factory.dimensions,
                                                self._fitness_func,
                                                *self._args,
                                                **self._kwargs)
        self._population += [genome_factory.build([base_genome]) for _ in range(n)]
        return self

    def add_to_initial_population(self, genome):
        self._population.append(genome)
        return self

    def build(self):
        for genome in self._population:
            genome.run()

        if len(self._population) < 1:
            raise InitialPopulationUndefinedException

        initial_candidate = self._population[self._rng.random_int(0, len(self._population))]

        new_optimizer = BasicAnnealingOptimizer(initial_candidate,
                                                self._new_candidate_genome_factory,
                                                self._annealing_schedule,
                                                self._rng)

        return new_optimizer

    def new_population(self):
        self._population = []
        return self

