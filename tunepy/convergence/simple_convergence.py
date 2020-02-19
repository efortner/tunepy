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
