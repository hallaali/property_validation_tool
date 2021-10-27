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
      headers = ['P_val', 'T_val', 'h_val_CEA', 's_val_CEA', 'k_val_CEA', 'mu_val_CEA', 'Cp_val_CEA', 'gam_val_CEA', 'rho_val_CEA', 'R_val_CEA', 'h_val_pkg', 's_val_pkg', 'k_val_pkg', 'mu_val_pkg', 'Cp_val_pkg', 'gam_val_pkg', 'rho_val_pkg', 'R_val_pkg', 'h_val_err', 's_val_err', 'k_val_err', 'mu_val_err', 'Cp_val_err', 'gam_val_err', 'rho_val_err', 'R_val_err', 'outlier_val']
      df = pd.read_csv(import_file_path, usecols=headers, sep=',')
      x = df['T_val']
      print(x)

browseButton = tk.Button(text='Load File...', command=getFile)
browseButton.grid(row=20, column=0)

plotButton = tk.Button(text='Plot', command=enthalpy_h)
plotButton.grid(row=20, column=2)

window.mainloop()
