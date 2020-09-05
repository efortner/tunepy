from abc import ABC, abstractmethod
from typing import List

from tunepy import Genome


class AbstractGenomeFactory(ABC):
    """ Interface for constructing new Genome objects based on prior Genomes """

    @abstractmethod
    def build(self, prior_genomes: List[Genome]) -> Genome:
        """ Builds a new Genome from a list of priors

        :param prior_genomes: list of prior Genomes
        :return: a new Genome object
        """
        pass

    @property
    @abstractmethod
    def dimensions(self) -> tuple:
        """

        :return: the dimensions of Genome objects returned by this factory
        """
        pass

