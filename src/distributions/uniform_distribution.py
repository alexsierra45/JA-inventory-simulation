from random import random
from distribution import Distribution

class UniformDistribution(Distribution):
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def generate_sample(self):
        return random.uniform(self.lower_bound, self.upper_bound)