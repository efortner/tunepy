from typing import List, Dict, Tuple

from tunepy import transform_bitstring_to_layers_tuple
from tunepy.interfaces import AbstractLearnerFactory, AbstractRandomNumberGenerator, AbstractLearner
from tunepy.learners import SklearnMlpClassifierLearner


class SklearnMlpClassifierFactory(AbstractLearnerFactory):
    """
    Transforms bitstrings into SklearnMlpClassifierLearner.
    """
    def __init__(
            self,
            *args,
            **kwargs):
        """
        Creates a new SklearnMlpClassifierFactory.

        :param args: will be passed into the MLPClassifier
        :param kwargs: will be passed into the MLPClassifier
        """
        self._args = args
        self._kwargs = kwargs

    def build(self, bitstring: Tuple) -> AbstractLearner:
        """
        Builds a new model object with hyperparameters derived from the provided bitstring

        :param bitstring: a bitstring representing hyperparameters for this model
        :return: a new, untrained learner
        """
        layers = transform_bitstring_to_layers_tuple(bitstring)
        return SklearnMlpClassifierLearner(layers=layers, *self._args, **self._kwargs)
