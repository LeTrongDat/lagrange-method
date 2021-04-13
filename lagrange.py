import numpy as np
class Lagrange:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def f(self, x):
        n = len(self.x)
        return sum(np.prod([(x-self.x[j])/(self.x[i]-self.x[j]) if j!=i else 1 for j in range(n)]) * self.y[i] for i in range(n))

