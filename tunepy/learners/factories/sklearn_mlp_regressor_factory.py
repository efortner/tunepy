from tunepy import transform_bitstring_to_layers_tuple
from tunepy.interfaces import AbstractLearnerFactory
from tunepy.learners import SklearnMlpRegressorLerner


class SklearnMlpRegressorFactory(AbstractLearnerFactory):
    def __init__(self, rng, *args, **kwargs):
        self._rng = rng
        self._args = args
        self._kwargs = kwargs

    def build(self, bitstring):
        layers = transform_bitstring_to_layers_tuple(bitstring)
        return SklearnMlpRegressorLerner(layers=layers, *self._args, **self._kwargs)
