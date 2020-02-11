from tunepy.interfaces import AbstractConvergenceCriterion


class Iterations(AbstractConvergenceCriterion):
    """
    Declares convergence after a set number of iterations.
    """

    def __init__(self, n):
        """
        This convergence criterion will return True after converged() has been called n times. If n=1, converged
        will return True immediately.
        :param n: An integer of the number of iterations allowed before declaring convergence.
        """
        self._n = n
        self._current_iteration = 1

    def converged(self, old_population, new_population):
        if self._current_iteration >= self._n:
            return True

        self._current_iteration += 1
        return False


class ExponentialDegradation(AbstractConvergenceCriterion):
    """
    Exponentially degrades a variable and returns converged when it falls below a threshold. This is useful
    for simulated annealing.
    """

    def __init__(self, initial_value=1.0, minimum_value=1e-5, degradation_rate=0.99):
        """
        Creates a new ExponentialDegradation convergence criterion.
        :param initial_value: Float representing the starting value for the exponential degradation.
        :param minimum_value: Float representing the threshold after which convergence is declared.
        :param degradation_rate: Float multiplied every time converged() is called. Must be within the interval [0, 1)
        """
        self._value = initial_value
        self._minimum_value = minimum_value
        self._degradation_rate = degradation_rate

    def converged(self, old_population, new_population):
        self._value *= self._degradation_rate
        if self._value < self._minimum_value:
            return True

        return False
