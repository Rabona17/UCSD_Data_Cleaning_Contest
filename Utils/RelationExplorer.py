import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class RelationExplorer():
    """
    Visualize the relation(positive/negative/none) between two rows
    """
    def __init__(self, dataframe, x_axis, y_axis):
        self.df = dataframe
        self.x = x_axis
        self.y = y_axis
    
    def plot_scatter(self, sample_size):
        sampled = self.df[self.df[self.x]!=0][self.df[self.y]!=0].sample(sample_size)
        plt.scatter(sampled[self.x], sampled[self.y])
        plt.show()