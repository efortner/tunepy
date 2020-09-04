from tunepy.interfaces import AbstractModelComparer


class PassThroughComparer(AbstractModelComparer):
    """
    Returns the first item passed into it.
    """

    def compare(self, genomes):
        """
        Compares a set of models naively.
        :param genomes: Array-like of genomes.
        :return: THe first model at the zero index of models.
        """
        return genomes[0]


class IncrementalComparer(AbstractModelComparer):
    """
    Returns the next item from the list.
    """

    def __init__(self):
        self._index = 0

    def compare(self, genomes):
        next_index = self._index % len(genomes)
        self._index += 1
        return genomes[next_index]
