from tunepy import Genome
from tunepy.interfaces import AbstractOptimizerBuilder
from tunepy.optimizers import BasicOptimizer


class BasicOptimizerBuilder(AbstractOptimizerBuilder):
    def __init__(self, dimensions, fitness_func, new_candidate_genome_builder, convergence_criterion, *args, **kwargs):
        self._dimensions = dimensions
        self._fitness_func = fitness_func
        self._new_candidate_genome_builder = new_candidate_genome_builder
        self._convergence_criterion = convergence_criterion
        self._args = args
        self._kwargs = kwargs

    def build_with_initial_population(self, initial_candidate_genome_builder):
        initial_genome = initial_candidate_genome_builder.build([Genome.new_default_genome(
            self._dimensions, self._fitness_func, *self._args, **self._kwargs
        )])
        initial_genome.run()
        return BasicOptimizer(initial_genome, self._new_candidate_genome_builder, self._convergence_criterion)
