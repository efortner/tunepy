from tunepy import Genome
from tunepy.optimizers.meta import BasicRestartOptimizer
from tunepy.optimizers import BasicAnnealingOptimizer, BasicOptimizer, BasicGeneticOptimizer
from tunepy.convergence import Iterations, ConsecutiveNonImprovement, ExponentialAnnealingSchedule
from tunepy.optimizers.builders import BasicOptimizerBuilder
from tunepy.genome_factory import RandomGenomeFactory, \
    RandomNeighborGenomeFactory, \
    SinglePointCrossoverGenomeFactory
from tunepy.random import NumpyRNG
from tunepy.comparison import RouletteWheelComparer


def new_random_restart_hill_climber(
        dimensions,
        restarts,
        convergence_iterations,
        epsilon,
        fitness_func,
        *args,
        **kwargs):
    random = NumpyRNG()

    random_genome_factory = \
        RandomGenomeFactory(
            dimensions,
            random,
            fitness_func,
            *args,
            **kwargs)

    neighbor_genome_factory = \
        RandomNeighborGenomeFactory(
            dimensions,
            random,
            1,
            fitness_func,
            *args,
            **kwargs)

    restart_convergence = Iterations(restarts)

    single_optimizer_convergence = ConsecutiveNonImprovement(convergence_iterations, epsilon)

    optimizer_builder = \
        BasicOptimizerBuilder(
            dimensions,
            random,
            neighbor_genome_factory,
            single_optimizer_convergence,
            fitness_func,
            *args,
            **kwargs)

    return BasicRestartOptimizer(
        optimizer_builder,
        random_genome_factory,
        1,
        restart_convergence)


def new_simulated_annealer(
        dimensions,
        max_neighbor_distance,
        initial_temperature,
        minimum_temperature,
        degradation_multiplier,
        fitness_func,
        *args,
        **kwargs):
    random = NumpyRNG()

    neighbor_genome_factory = \
        RandomNeighborGenomeFactory(
            dimensions,
            random,
            max_neighbor_distance,
            fitness_func,
            *args,
            **kwargs)

    annealing_schedule = \
        ExponentialAnnealingSchedule(
            initial_temperature,
            minimum_temperature,
            degradation_multiplier)

    initial_candidate = \
        Genome.new_default_genome(
            dimensions,
            fitness_func,
            *args,
            **kwargs)

    initial_candidate.run()

    return BasicAnnealingOptimizer(
        initial_candidate,
        neighbor_genome_factory,
        annealing_schedule,
        random)


def new_hill_climber(
        dimensions,
        convergence_iterations,
        epsilon,
        fitness_func,
        *args,
        **kwargs):
    random = NumpyRNG()

    neighbor_genome_factory = \
        RandomNeighborGenomeFactory(
            dimensions,
            random,
            1,
            fitness_func,
            *args,
            **kwargs)

    initial_candidate = \
        Genome.new_default_genome(
            dimensions,
            fitness_func,
            *args,
            **kwargs)

    initial_candidate.run()

    convergence_criterion = ConsecutiveNonImprovement(convergence_iterations, epsilon)

    return BasicOptimizer(
        initial_candidate,
        neighbor_genome_factory,
        convergence_criterion)


def new_genetic_optimizer(
        dimensions,
        population_size,
        mutation_rate,
        convergence_iterations,
        epsilon,
        fitness_func,
        *args,
        **kwargs):
    random = NumpyRNG()

    comparer = RouletteWheelComparer(random)

    genome_factory = \
        SinglePointCrossoverGenomeFactory(
            dimensions,
            random,
            mutation_rate,
            comparer,
            fitness_func,
            *args,
            **kwargs)

    initial_population_genome_factory = \
        RandomGenomeFactory(
            dimensions,
            random,
            fitness_func,
            *args,
            **kwargs)

    convergence_criterion = ConsecutiveNonImprovement(convergence_iterations, epsilon)

    initial_population = []

    for _ in range(population_size):
        new_genome = initial_population_genome_factory.build([])
        new_genome.run()
        initial_population.append(new_genome)

    return BasicGeneticOptimizer(
        initial_population,
        genome_factory,
        convergence_criterion)
