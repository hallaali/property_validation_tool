import tkinter as tk
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)




# The main tkinter window
window = Tk()
window.geometry("500x200")
# setting the title
window.title('Property Package Validation')

title1 = Label(window, text="Pratt & Whitney")
title1.grid(row=0,column=0)


def getFile():
      global df
      import_file_path = filedialog.askopenfilename()
      df = pd.read(import_file_path)

browseButton = tk.Button(text='Load File...', command=getFile)
browseButton.grid(row=20, column=2)

window.mainloop()
