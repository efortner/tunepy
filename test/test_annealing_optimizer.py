import unittest

from tunepy.interfaces.stubs import PassThroughConvergenceCriterion, PassThroughGenomeBuilder, NumpyCustomRandom
from tunepy.optimizers import BasicAnnealingOptimizer
from tunepy.internal import Genome


class TestAnnealingOptimizer(unittest.TestCase):
    def test_worse_solution_acceptance(self):
        def fitness_func_zero(bitstring):
            return 0

        def fitness_func_one(bitstring):
            return 1

        initial_candidate = Genome(fitness_func_one, [0])
        convergence_criterion = PassThroughConvergenceCriterion(True)
        genome_builder = PassThroughGenomeBuilder(Genome(fitness_func_zero, [1]))
        rng = NumpyCustomRandom(0.0, 1)
        optimizer = BasicAnnealingOptimizer(initial_candidate, genome_builder, convergence_criterion, rng)

        optimizer.next()

        self.assertEqual(0, optimizer.best_genome.fitness)

    def test_better_solution_acceptance(self):
        def fitness_func_zero(bitstring):
            return 0

        def fitness_func_one(bitstring):
            return 1

        initial_candidate = Genome(fitness_func_zero, [0])
        convergence_criterion = PassThroughConvergenceCriterion(True)
        genome_builder = PassThroughGenomeBuilder(Genome(fitness_func_one, [1]))
        rng = NumpyCustomRandom(0.0, 1)
        optimizer = BasicAnnealingOptimizer(initial_candidate, genome_builder, convergence_criterion, rng)

        optimizer.next()

        self.assertEqual(1, optimizer.best_genome.fitness)

    def test_convergence(self):
        def fitness_func_zero(bitstring):
            return 0

        initial_candidate = Genome(fitness_func_zero, [0])
        convergence_criterion = PassThroughConvergenceCriterion(True)
        genome_builder = PassThroughGenomeBuilder(Genome(fitness_func_zero, [1]))
        rng = NumpyCustomRandom(0.0, 1)
        optimizer = BasicAnnealingOptimizer(initial_candidate, genome_builder, convergence_criterion, rng)

        self.assertFalse(optimizer.converged)
        optimizer.next()
        self.assertTrue(optimizer.converged)


if __name__ == '__main__':
    unittest.main()
