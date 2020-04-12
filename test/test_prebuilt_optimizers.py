import unittest
from tunepy import new_random_restart_hill_climber, new_simulated_annealer
from tunepy.optimizers.meta import BasicRestartOptimizer
from tunepy.optimizers import BasicAnnealingOptimizer


class TestPrebuiltOptimizers(unittest.TestCase):
    def test_creates_random_restart_hill_climber(self):
        def fitness_func(bitstring):
            return 69.0

        optimizer = new_random_restart_hill_climber((5,),
                                                    7,
                                                    10,
                                                    1e-5,
                                                    fitness_func)

        self.assertIsInstance(optimizer, BasicRestartOptimizer)
        self.assertFalse(optimizer.converged)

        for _ in range(6):
            optimizer.next()
            self.assertFalse(optimizer.converged)
            self.assertAlmostEqual(optimizer.best_genome.fitness, 69.0)

        optimizer.next()
        self.assertTrue(optimizer.converged)

    def test_creates_simulated_annealer(self):
        def fitness_func(bitstring):
            return 69.0

        optimizer = new_simulated_annealer((5,),
                                           1,
                                           10,
                                           3,
                                           0.5,
                                           fitness_func)

        self.assertIsInstance(optimizer, BasicAnnealingOptimizer)
        self.assertFalse(optimizer.converged)

        for _ in range(2):
            optimizer.next()
            self.assertFalse(optimizer.converged)
            self.assertAlmostEqual(optimizer.best_genome.fitness, 69.0)

        optimizer.next()
        self.assertTrue(optimizer.converged)


if __name__ == '__main__':
    unittest.main()
