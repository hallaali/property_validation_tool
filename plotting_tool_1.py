from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import sys 

def twoD_plot1(x, y, title, xlabel, ylabel):
    fig = plt.figure()
    plot1 = fig.add_subplot(111)
    plot1.plot(x, y)
    plot1.set_title(title)
    plot1.set_xlabel(xlabel)
    plot1.set_ylabel(ylabel)
    plt.show()


def twoD_plot2(x, y1, y2, title, xlabel, ylabel, y1_label, y2_label):
    fig = plt.figure()
    plot1 = fig.add_subplot(111)
    plot1.plot(x, y1, label= y1_label)
    plot1.plot(x, y2, label=y2_label)
    plot1.set_title(title)
    plot1.set_xlabel(xlabel)
    plot1.set_ylabel(ylabel)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])
