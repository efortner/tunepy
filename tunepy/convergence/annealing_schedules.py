from tunepy.interfaces import AbstractAnnealingSchedule


class ExponentialAnnealingSchedule(AbstractAnnealingSchedule):
    def __init__(self, initial_temperature, minimum_temperature, degradation_multiplier):
        self._temperature = initial_temperature
        self._minimum_temperature = minimum_temperature
        self._degradation_multiplier = degradation_multiplier

    @property
    def temperature(self):
        return self._temperature

    def converged(self, old_population, new_population):
        return_value = self._temperature < self._minimum_temperature
        self._temperature *= self._degradation_multiplier
        return return_value
