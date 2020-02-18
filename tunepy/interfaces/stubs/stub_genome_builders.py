from tunepy.interfaces import AbstractGenomeBuilder
from copy import deepcopy


class PassThroughGenomeBuilder(AbstractGenomeBuilder):
    def __init__(self, returned_genome):
        self._genome = returned_genome

    def build(self, prior_genomes):
        return deepcopy(self._genome)
