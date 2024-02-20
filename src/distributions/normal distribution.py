import numpy as np
from distribution import Distribution

class NormalDistribution(Distribution):
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    def generate_sample(self):
        return max(0, np.random.normal(self.mean, self.std_dev))