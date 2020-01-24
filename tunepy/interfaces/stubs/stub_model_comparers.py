from tunepy.interfaces import AbstractModelComparer


class PassThroughComparer(AbstractModelComparer):
    """
    Returns its input during comparison.
    """

    def compare(self, models):
        return models
