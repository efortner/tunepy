from tunepy.optimizers.meta import BasicRestartOptimizer
from tunepy.interfaces import AbstractOptimizer
from tunepy.convergence import Iterations, ConsecutiveNonImprovement
from tunepy.optimizers.builders import BasicOptimizerBuilder
from tunepy.genome_factory import RandomGenomeFactory, RandomNeighborGenomeFactory
from tunepy.random import NumpyRNG


class RandomRestartHillClimber(AbstractOptimizer):
    def __init__(self, dimensions, restarts, fitness_func, convergence_iterations, epsilon, *args, **kwargs):
        random = NumpyRNG()

        random_genome_factory = RandomGenomeFactory(
            random,
            fitness_func,
            *args,
            **kwargs
        )

        neighbor_genome_factory = RandomNeighborGenomeFactory(
            dimensions,
            random,
            fitness_func,
            *args,
            **kwargs
        )

        restart_convergence = Iterations(restarts)

        single_optimizer_convergence = ConsecutiveNonImprovement(
            convergence_iterations,
            epsilon
        )

        optimizer_builder = BasicOptimizerBuilder(
            dimensions,
            fitness_func,
            neighbor_genome_factory,
            single_optimizer_convergence,
            *args,
            **kwargs
        )

        self._restart_optimizer = BasicRestartOptimizer(
            optimizer_builder,
            random_genome_factory,
            1,
            restart_convergence
        )

    def next(self):
        self._restart_optimizer.next()

    @property
    def converged(self):
        return self._restart_optimizer.converged

    @property
    def best_genome(self):
        return self._restart_optimizer.best_genome
