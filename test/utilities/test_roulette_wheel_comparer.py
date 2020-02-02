import unittest
from tunepy.comparers import RouletteWheelComparer
from tunepy.interfaces.stubs import NumpyPassThroughRandom, NumpyOnesRandom, ConstantFitnessLearner


class TestRouletteWheelComparer(unittest.TestCase):

    def test_fitness_extraction(self):
        rng = NumpyOnesRandom()
        comparer = RouletteWheelComparer(rng)
        models = [ConstantFitnessLearner(10-index) for index in range(10)]
        fitnesses = comparer._extract_fitness_from_models(models)

        self.assertEqual(10, len(models))
        self.assertEqual(1, fitnesses[0])
        self.assertEqual(10, fitnesses[-1])

if __name__ == '__main__':
    unittest.main()
