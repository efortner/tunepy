from tunepy.interfaces import AbstractModelComparer
import numpy as np


class RouletteWheelComparer(AbstractModelComparer):
    """
    Performs a fitness proportionate random model selection.
    """

    def compare(self, models):
        pass