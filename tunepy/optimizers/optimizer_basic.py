from tunepy.interfaces import AbstractOptimizer


class BasicOptimizer(AbstractOptimizer):
    def __init__(self, initial_candidate, genome_factory, convergence_criterion):
        self._candidate = initial_candidate
        self._genome_factory = genome_factory
        self._convergence_criterion = convergence_criterion
        self._converged = False

    def next(self):
        old_candidate = self._candidate
        new_candidate = self._genome_factory.build([old_candidate])
        new_candidate.run()
        if new_candidate.fitness > old_candidate.fitness:
            self._candidate = new_candidate

        self._converged = self._convergence_criterion.converged(old_candidate, new_candidate)

    @property
    def converged(self):
        return self._converged

    @property
    def best_genome(self):
        return self._candidate
