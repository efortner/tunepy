from tunepy.interfaces import AbstractModelComparer


class PassThroughComparer(AbstractModelComparer):
    """
    Returns the first item passed into it.
    """

    def compare(self, models):
        """
        Compares a set of models naively.
        :param models: Array-like of models.
        :return: THe first model at the zero index of models.
        """
        return models[0]
