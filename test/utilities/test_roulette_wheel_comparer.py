import unittest
from tunepy.comparers import RouletteWheelComparer
from tunepy.interfaces import AbstractRandomNumberGenerator
from tunepy.interfaces.stubs import NumpyOnesRandom, ConstantFitnessLearner


class TestRouletteWheelComparer(unittest.TestCase):

    def test_returns_best_model(self):
        class CustomRandom(AbstractRandomNumberGenerator):

            def random_int_array(self, minimum, maximum, shape):
                return [0]

            def random(self):
                return 0.0

        rng = CustomRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        returned_model = comparer.compare(models)
        self.assertEqual(10, returned_model.fitness)

    def test_returns_worst_model(self):
        class CustomRandom(AbstractRandomNumberGenerator):

            def random_int_array(self, minimum, maximum, shape):
                return [9]

            def random(self):
                return 0.0

        rng = CustomRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        returned_model = comparer.compare(models)
        self.assertEqual(1, returned_model.fitness)

    def test_returns_median_model(self):
        class CustomRandom(AbstractRandomNumberGenerator):

            def random_int_array(self, minimum, maximum, shape):
                return [5]

            def random(self):
                return 0.0

        rng = CustomRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        returned_model = comparer.compare(models)
        self.assertEqual(5, returned_model.fitness)

    def test_cached_fitness(self):
        rng = NumpyOnesRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        first_check = comparer._extract_fitness_from_genomes(models)
        second_check = comparer._extract_fitness_from_genomes(models)

        self.assertTrue(first_check)
        self.assertFalse(second_check)
        self.assertAlmostEqual(10, comparer._max_fitness)

if __name__ == '__main__':
    unittest.main()
