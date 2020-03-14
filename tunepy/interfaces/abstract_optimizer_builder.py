from abc import ABC, abstractmethod


class AbstractOptimizerBuilder(ABC):

    @abstractmethod
    def add_to_initial_population_from_factory(self, genome_factory, n):
        pass

    @abstractmethod
    def add_to_initial_population(self, genome):
        pass

    @abstractmethod
    def build(self):
        pass
