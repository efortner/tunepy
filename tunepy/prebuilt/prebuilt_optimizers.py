from tunepy import Genome
from tunepy.optimizers.meta import BasicRestartOptimizer
from tunepy.optimizers import BasicAnnealingOptimizer
from tunepy.convergence import Iterations, ConsecutiveNonImprovement, ExponentialAnnealingSchedule
from tunepy.optimizers.builders import BasicOptimizerBuilder
from tunepy.genome_factory import RandomGenomeFactory, RandomNeighborGenomeFactory
from tunepy.random import NumpyRNG


def new_random_restart_hill_climber(dimensions,
                                    restarts,
                                    convergence_iterations,
                                    epsilon,
                                    fitness_func,
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
                                              neighbor_genome_factory,
                                              single_optimizer_convergence,
                                              fitness_func,
                                              *args,
                                              **kwargs)

    return BasicRestartOptimizer(optimizer_builder,
                                 random_genome_factory,
                                 1,
                                 restart_convergence)


def new_simulated_annealer(dimensions,
                           max_neighbor_distance,
                           initial_temperature,
                           minimum_temperature,
                           degradation_multiplier,
                           fitness_func,
                           *args,
                           **kwargs):
    random = NumpyRNG()

    neighbor_genome_factory = RandomNeighborGenomeFactory(dimensions,
                                                          random,
                                                          fitness_func,
                                                          max_neighbor_distance,
                                                          *args,
                                                          **kwargs)

    annealing_schedule = ExponentialAnnealingSchedule(initial_temperature,
                                                      minimum_temperature,
                                                      degradation_multiplier)

    initial_candidate = Genome.new_default_genome(dimensions,
                                                  fitness_func,
                                                  *args,
                                                  **kwargs)

    return BasicAnnealingOptimizer(initial_candidate,
                                   neighbor_genome_factory,
                                   annealing_schedule,
                                   random)
