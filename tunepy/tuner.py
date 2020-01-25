

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
            :param model_builder: An object that builds learners.
            """
            self.bundle = {
                'x': x,
                'y': y,
                'builder': model_builder,
            }

        def build(self):
            """
            Creates a new instance of Tuner container the properties specified by the builder.
            :return: A new instance of Tuner.
            """
            return Tuner(self.bundle)

    def __init__(self, bundle):
        pass
