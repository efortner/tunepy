from abc import ABC, abstractmethod


class AbstractGenomeBuilder(ABC):
    """
    Builds Genome objects.
    """

    @abstractmethod
    def build(self, prior_genomes):
        """
        Builds a single new genome.
        :param prior_genomes: Iterable of a Genome objects.
        :return: A new Genome object.
        """
        pass
