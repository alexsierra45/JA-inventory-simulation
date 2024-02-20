from random import random
from distribution import Distribution

class PoissonDistribution(Distribution):
    def __init__(self, rate):
        self.rate = rate

    def generate_sample(self):
        return random.poisson(self.rate)