import unittest
from tunepy.interfaces.stubs import IncrementalComparer, NumpyOnesRandom
from tunepy.internal import GeneticAlgorithmGenomeBuilder, DimensionsMismatchException


class TestGeneticAlgorithmGenomeBuilder(unittest.TestCase):
    def test_incorrect_dimensions_passed_in(self):
        def fitness_func(bitstring):
            return 0.0

        left = [0, 0, 0, 0, 0, ]
        right = [1, 1, 1, 1, 1, ]
        dimensions = (4,)

        comparer = IncrementalComparer()
        rng = NumpyOnesRandom()
        genome_builder = GeneticAlgorithmGenomeBuilder(dimensions, rng, 0.0, comparer, fitness_func)

        with self.assertRaises(DimensionsMismatchException):
            genome_builder.build([left, right])


if __name__ == '__main__':
    unittest.main()
