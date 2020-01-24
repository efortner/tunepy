from tunepy.interfaces import AbstractOptimizer


class ConvergedOptimizer(AbstractOptimizer):
    """
    Always appears to have converged.
    """

    @property
    def converged(self):
        return True

    def next(self):
        pass
