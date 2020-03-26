import unittest

from tunepy.optimizers import BasicOptimizer
from tunepy.optimizers.builders import BasicOptimizerBuilder
from tunepy.interfaces.stubs import PassThroughConvergenceCriterion
from tunepy.interfaces.stubs import PassThroughGenomeFactory
from tunepy import Genome, InitialPopulationUndefinedException


class TestOptimizerBasicBuilder(unittest.TestCase):
    def test_add_to_initial_population_from_factory_returns_self(self):
        def fitness_func(bitstring):
            self.fail()

        genome_factory = PassThroughGenomeFactory(Genome.new_default_genome((5,), fitness_func))
        convergence_criterion = PassThroughConvergenceCriterion(True)
        optimizer_builder = BasicOptimizerBuilder((5,), fitness_func, genome_factory, convergence_criterion)

        returned_object = optimizer_builder.add_to_initial_population_from_factory(genome_factory, 1)
        self.assertIs(optimizer_builder, returned_object)

    def test_add_to_initial_population_returns_self(self):
        def fitness_func(bitstring):
            self.fail()

        genome_factory = PassThroughGenomeFactory(Genome.new_default_genome((5,), fitness_func))
        convergence_criterion = PassThroughConvergenceCriterion(True)
        optimizer_builder = BasicOptimizerBuilder((5,), fitness_func, genome_factory, convergence_criterion)

        returned_object = optimizer_builder.add_to_initial_population(Genome.new_default_genome((5,), fitness_func))
        self.assertIs(optimizer_builder, returned_object)

    def test_add_to_initial_population_from_factory_successful(self):
        def fitness_func(bitstring):
            return 69.0

        genome_factory = PassThroughGenomeFactory(Genome.new_default_genome((5,), fitness_func))
        convergence_criterion = PassThroughConvergenceCriterion(True)
        optimizer_builder = BasicOptimizerBuilder((5,), fitness_func, genome_factory, convergence_criterion)

        optimizer = optimizer_builder \
            .add_to_initial_population_from_factory(genome_factory, 1) \
            .build()

        self.assertAlmostEqual(optimizer.best_genome.fitness, 69.0)
        self.assertIsInstance(optimizer, BasicOptimizer)

    def test_add_to_initial_population_successful(self):
        class SpyFitnessFunc:
            def __init__(self):
                self.fitness_func_executions = 0

            def fitness_func(self, bitstring):
                self.fitness_func_executions += 1
                return 69.0

        unused_spy_fitness_function_holder = SpyFitnessFunc()
        genome_factory = PassThroughGenomeFactory(
            Genome.new_default_genome((5,), unused_spy_fitness_function_holder.fitness_func))
        convergence_criterion = PassThroughConvergenceCriterion(True)
        optimizer_builder = BasicOptimizerBuilder((5,), unused_spy_fitness_function_holder.fitness_func, genome_factory,
                                                  convergence_criterion)

        spy_fitness_function_holder = SpyFitnessFunc()
        population_genome = Genome(spy_fitness_function_holder.fitness_func, [0, 0, 0, 0, 0])

        optimizer = optimizer_builder \
            .add_to_initial_population(population_genome) \
            .build()

        self.assertAlmostEqual(optimizer.best_genome.fitness, 69.0)
        self.assertEqual(spy_fitness_function_holder.fitness_func_executions, 1)
        self.assertIsInstance(optimizer, BasicOptimizer)

    def test_build_raises_exception_with_no_population(self):
        def fitness_func(bitstring):
            self.fail()

        genome_factory = PassThroughGenomeFactory(
            Genome.new_default_genome((5,), fitness_func))
        convergence_criterion = PassThroughConvergenceCriterion(True)
        optimizer_builder = BasicOptimizerBuilder((5,), fitness_func, genome_factory, convergence_criterion)

        with self.assertRaises(InitialPopulationUndefinedException):
            optimizer_builder.build()


if __name__ == '__main__':
    unittest.main()
