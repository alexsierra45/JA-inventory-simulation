import numpy as np
from .distribution import Distribution

class PoissonDistribution(Distribution):
    def __init__(self, rate):
        self.rate = rate

    def generate_sample(self):
        return np.random.poisson(self.rate)