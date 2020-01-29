from tunepy.random import PythonBaseRNG


class Tuner:
    """
    A generic supervised learning hyperparameter tuner.
    """

    class Builder:
        """
        Builds a new customized instance of Tuner.
        """

        def __init__(self, x, y, model_builder):
            """
            Creates a new Tuner.Builder.
            :param x: Array-like data set features.
            :param y: Vector of data set labels.
            :param model_builder: An object that builds learners. Must comply to tunepy's AbstractModelBuilder
            interface.
            """
            self._bundle = {
                'x': x,
                'y': y,
                'builder': model_builder,
                'rng': PythonBaseRNG,
                'optimizer': None,
            }

        def set_rng(self, rng):
            """
            Sets the random number generator that will be used. Must comply to tunepy's AbstractRandomNumberGenerator
            interface.
            :param rng: A object of a class that implements AbstractRandomNumberGenerator.
            :return: This builder.
            """
            self._bundle['rng'] = rng
            return self

        def set_optimizer(self, optimizer):
            """
            Sets the hyperparameter optimizer that will be used.
            :param optimizer: An optimizer object of a class that implement's tunepy's AbstractOptimizer interface.
            :return: This builder.
            """
            self._bundle['optimizer'] = optimizer
            return self

        def build(self):
            """
            Creates a new instance of Tuner container the properties specified by the builder.
            :return: A new instance of Tuner.
            """
            return Tuner(self._bundle)

    def __init__(self, bundle):
        """
        Use Tuner.Builder to create instances of Tuner.
        :param bundle: An object created by Tuner.Builder.
        """
        self._x = bundle['x']
        self._y = bundle['y']
        self._model_builder = bundle['builder']
        self._rng = bundle['rng']
        self._optimizer = bundle['optimizer']
