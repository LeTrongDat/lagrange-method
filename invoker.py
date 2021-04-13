import numpy as np 
from random import random
from pandas import DataFrame
from matplotlib import pyplot as plt

from function import Function
from lagrange import Lagrange
class COLOR:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log(string, color = ""):
    print(color + string + COLOR.ENDC, end = "")

class Invoker:
    DASH = "-" * 20
    MAX_RANDOM_NUMBER = 100
    def __init__(self):
        pass 
    def invoke(self):
        functions = [
            Function("y = sin(x)", lambda x: np.sin(x)),
            Function("y = sin(x) + cos(x)", lambda x: np.sin(x) + np.cos(x)),
            Function("y = 3x^3 - 2x^2 + 2", lambda x: 3*np.power(x, 3) - 2*np.power(x, 2)+2)
        ]
        log("> {} Welcome to interpolation world {}\n".format(self.DASH, self.DASH), COLOR.HEADER)
        log("> Please choose your function:\n", COLOR.OKGREEN)
        for i, func in enumerate(functions):
            print("> {}. {}".format(i, func.to_str()))
        log("> Enter your option: ", COLOR.OKGREEN)
        opt_func = int(input())

        chosen_func = functions[opt_func]

        log(self.DASH * 3 + '\n', COLOR.HEADER)
        log("> Please choose the way to generate interpolation points: \n", COLOR.OKGREEN)
        log("> 0. Manual\n")
        log("> 1. Auto generate (random points)\n")
        log("> Enter your option: ", COLOR.OKGREEN)
        opt_gene = int(input())

        x = self.generate(opt_gene)
        y_org = chosen_func.f(x)

        lagrange = Lagrange(x, y_org)
        y_lag = [lagrange.f(xi) for xi in x]

        self.draw(x, y_org, y_lag, chosen_func, lagrange)
    def generate(self, opt):
        if opt == 0:
            log("> Enter x(s): ", COLOR.OKGREEN)
            x = list(map(int, input().split()))
            return x
        log("> Enter a number of points: ", COLOR.OKGREEN)
        num_pts = int(input())
        x = [random() * self.MAX_RANDOM_NUMBER for i in range(num_pts)]
        return x
    def draw(self, x, y_org, y_lag, chosen_func, lagrange):
        fig, axs = plt.subplots(2)
        for i in range(2):
            axs[i].grid(True)

        x1 = np.arange(min(x) - 1, max(x) + 1, 0.1)
        y1_org = chosen_func.f(x1)
        y1_lag = [lagrange.f(xi) for xi in x1]

        axs[0].plot(x1, y1_org, label = chosen_func.to_str(), ls = "dashed") 
        axs[0].scatter(x, y_org, marker = '.', color = 'r', s = 100)
        axs[0].legend(loc = "center left")

        axs[1].plot(x1, y1_lag, label = "lagrange function", ls = "dashed")
        axs[1].scatter(x, y_lag, marker = '.', color = 'r', s = 100)
        axs[1].legend(loc = "center left")

        plt.show()