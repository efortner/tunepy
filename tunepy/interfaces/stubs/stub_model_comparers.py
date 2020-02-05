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
