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


class ConsecutiveNonImprovement(AbstractConvergenceCriterion):
    def __init__(self, n, epsilon):
        self._last_iteration = n - 1
        self._iteration_count = 0
        self._epsilon = epsilon
        self._net_improvement = 0.0

    def converged(self, old_population, new_population):
        if self._net_improvement < self._epsilon and self._iteration_count == self._last_iteration:
            return True

        old_fitness = get_best_fitness(old_population)
        new_fitness = get_best_fitness(new_population)

        if self._iteration_count == 0:
            self._net_improvement = new_fitness - old_fitness
        else:
            self._net_improvement += new_fitness - old_fitness

        if self._net_improvement < self._epsilon:
            self._iteration_count += 1
        else:
            self._iteration_count = 0

        return False


def get_best_fitness(population):
    best_fitness = float('-inf')
    for genome in population:
        if genome.fitness > best_fitness:
            best_fitness = genome.fitness
    return best_fitness
