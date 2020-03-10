from abc import ABC, abstractmethod


class AbstractOptimizerBuilder(ABC):

    @abstractmethod
    def build_with_initial_population(self, genome_builder):
        pass
