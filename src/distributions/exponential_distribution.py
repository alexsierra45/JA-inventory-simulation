from random import random
from distribution import Distribution

class ExponentialDistribution(Distribution):
    def __init__(self, rate):
        self.rate = rate

    def generate_sample(self):
        return random.expovariate(self.rate)