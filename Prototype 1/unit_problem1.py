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

def enthalpy_h():
      fig = plt.figure()
      plot1 = fig.add_subplot(111)
      x = df['T_val']
      h_val_pkg = df['h_val_pkg']
      h_val_CEA = df['h_val_CEA']
      plot1.plot(x, h_val_pkg, marker='o', color='green', label='h_val_pkg')
      plot1.plot(x, h_val_CEA, color='blue', label='h_val_CEA')
      plot1.set_title('Enthalpy (h) Validation')
      plot1.set_xlabel('Temperature, T [R]')
      plot1.set_ylabel('Enthalpy, h [BTU/lbm]')
      plot1.legend()
      plt.show()


def getFile():
      global df
      import_file_path = filedialog.askopenfilename()
      headers = ['T_val', 'h_val_CEA', 'h_val_pkg']
      df = pd.read_csv(import_file_path, skiprows=1, usecols=headers, sep=' ')

browseButton = tk.Button(text='Load File...', command=getFile)
browseButton.grid(row=20, column=0)

plotButton = tk.Button(text='Plot', command=enthalpy_h)
plotButton.grid(row=20, column=2)

window.mainloop()
