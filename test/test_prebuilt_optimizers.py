import unittest
from tunepy import new_random_restart_hill_climber
from tunepy.optimizers.meta import BasicRestartOptimizer


class TestPrebuiltOptimizers(unittest.TestCase):
    def test_creates_random_restart_hill_climber(self):
        def fitness_func(bitstring):
            return 69.0

        optimizer = new_random_restart_hill_climber((5,),
                                                    7,
                                                    fitness_func,
                                                    10,
                                                    1e-5)

        self.assertIsInstance(optimizer, BasicRestartOptimizer)
        self.assertFalse(optimizer.converged)

        for _ in range(6):
            optimizer.next()
            self.assertFalse(optimizer.converged)
            self.assertAlmostEqual(optimizer.best_genome.fitness, 69.0)

        optimizer.next()
        self.assertTrue(optimizer.converged)


if __name__ == '__main__':
    unittest.main()
