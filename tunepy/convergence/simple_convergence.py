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

    def converged(self, old_candidate, new_candidate):
        if self._current_iteration >= self._n:
            return True

        self._current_iteration += 1
        return False


class ConsecutiveNonImprovement(AbstractConvergenceCriterion):
    def __init__(self, n, epsilon):
        self._last_iteration = n - 1
        self._iteration_count = 0
        self._epsilon = epsilon
        self._net_improvement = 0.0

    def converged(self, old_candidate, new_candidate):
        if self._net_improvement < self._epsilon and self._iteration_count == self._last_iteration:
            return True

        old_fitness = old_candidate.fitness
        new_fitness = new_candidate.fitness

        if self._iteration_count == 0:
            self._net_improvement = new_fitness - old_fitness
        else:
            self._net_improvement += new_fitness - old_fitness

        if self._net_improvement < self._epsilon:
            self._iteration_count += 1
        else:
            self._iteration_count = 0

        return False
