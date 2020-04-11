from tunepy.optimizers.meta import BasicRestartOptimizer
from tunepy.convergence import Iterations, ConsecutiveNonImprovement
from tunepy.optimizers.builders import BasicOptimizerBuilder
from tunepy.genome_factory import RandomGenomeFactory, RandomNeighborGenomeFactory
from tunepy.random import NumpyRNG


def new_random_restart_hill_climber(dimensions,
                                    restarts,
                                    fitness_func,
                                    convergence_iterations,
                                    epsilon,
                                    *args,
                                    **kwargs):
    random = NumpyRNG()

    random_genome_factory = RandomGenomeFactory(random,
                                                dimensions,
                                                fitness_func,
                                                *args,
                                                **kwargs)

    neighbor_genome_factory = RandomNeighborGenomeFactory(dimensions,
                                                          random,
                                                          fitness_func,
                                                          *args,
                                                          **kwargs)

    restart_convergence = Iterations(restarts)

    single_optimizer_convergence = ConsecutiveNonImprovement(convergence_iterations, epsilon)

    optimizer_builder = BasicOptimizerBuilder(dimensions,
                                              fitness_func,
                                              neighbor_genome_factory,
                                              single_optimizer_convergence,
                                              *args,
                                              **kwargs)

    return BasicRestartOptimizer(optimizer_builder,
                                 random_genome_factory,
                                 1,
                                 restart_convergence)
