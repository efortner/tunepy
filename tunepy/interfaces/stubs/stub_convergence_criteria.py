from tunepy.interfaces import AbstractConvergenceCriterion


class PassThroughConvergenceCriterion(AbstractConvergenceCriterion):
    """
    Returns the value passed in during instantiation.
    """

    def converged(self, old_population, new_population):
        return self._return_value

    def __init__(self, return_value):
        self._return_value = return_value

