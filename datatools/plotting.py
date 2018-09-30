from __future__ import division, print_function

import matplotlib

from abc import ABC
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


class PlotterBase(ABC):
    def __init__(self, figsize=(14, 7), fontsize=14):
        pass

    def scatterplot(self, x_data, y_data, x_label, y_label, title):
        pass


class MatplotlibPlotter(PlotterBase):
    def __init__(self, figsize=(14, 7), fontsize=14):
        matplotlib.rc('figure', figsize=figsize)
        matplotlib.rc('font', size=fontsize)
        matplotlib.rc('axes.spines', top=False, right=False)
        matplotlib.rc('axes', grid=False)
        matplotlib.rc('axes', facecolor='white')

    def scatterplot(self, x_data, y_data, x_label, y_label, title):
        _, ax = plt.subplots()
        ax.scatter(x_data, y_data, s=30, color='#539caf', alpha=0.75)
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

