import unittest
from tunepy.comparers import RouletteWheelComparer
from tunepy.interfaces.stubs import NumpyPassThroughRandom, NumpyOnesRandom, ConstantFitnessLearner


class TestRouletteWheelComparer(unittest.TestCase):

    def test_fitness_extraction(self):
        rng = NumpyOnesRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]
        comparer._extract_fitness_from_models(models)
        fitnesses = comparer._all_fitness

        self.assertEqual(10, len(fitnesses))
        self.assertEqual(1, fitnesses[0])
        self.assertEqual(10, fitnesses[-1])

    def test_multiple_fitness_extraction(self):
        rng = NumpyOnesRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        first_extraction = comparer._extract_fitness_from_models(models)
        second_extraction = comparer._extract_fitness_from_models(models)

        self.assertTrue(first_extraction)
        self.assertFalse(second_extraction)

    def test_returns_best_model(self):
        rng = NumpyOnesRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        returned_model = comparer.compare(models)
        self.assertEqual(10, returned_model.fitness)

    def test_returns_worst_model(self):
        rng = NumpyPassThroughRandom(0.0)
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        returned_model = comparer.compare(models)
        self.assertEqual(1, returned_model.fitness)

    def test_returns_median_model(self):
        rng = NumpyPassThroughRandom(0.5)
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10 - index) for index in range(10)]

        returned_model = comparer.compare(models)
        self.assertEqual(5, returned_model.fitness)


if __name__ == '__main__':
    unittest.main()
