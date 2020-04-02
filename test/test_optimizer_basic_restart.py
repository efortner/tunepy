import unittest

from tunepy.optimizers.meta import BasicRestartOptimizer
from tunepy.optimizers.builders import BasicOptimizerBuilder
from tunepy.interfaces.stubs import PassThroughGenomeFactory, PassThroughConvergenceCriterion
from tunepy import Genome


class TestOptimizerBasicRestart(unittest.TestCase):
    def test_convergence(self):
        def fitness_func(bitstring):
            return 69.0

        new_population_genome_factory = PassThroughGenomeFactory(
            Genome.new_default_genome(
                (5,),
                fitness_func
            )
        )
        convergence_criterion = PassThroughConvergenceCriterion(True)
        optimizer_builder = BasicOptimizerBuilder(
            (5,),
            fitness_func,
            new_population_genome_factory,
            convergence_criterion
        )

        meta_optimizer = BasicRestartOptimizer(
            optimizer_builder,
            new_population_genome_factory,
            10,
            convergence_criterion
        )

        meta_optimizer.next()
        self.assertAlmostEqual(meta_optimizer.best_genome.fitness, 69.0)
        self.assertTrue(meta_optimizer.converged)


if __name__ == '__main__':
    unittest.main()
