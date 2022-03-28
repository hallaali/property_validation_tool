import tkinter as tk
from tkinter import *
from tkinter.ttk import *
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
window.geometry("800x200")
# setting the title
window.title('Property Package Validation')

title1 = Label(window, text="Pratt & Whitney")
title1.grid(row=0,column=0)


label = Label(window, text="Enter Folder Name")
entry = Entry(window)
label.grid(row=20,column=0)
entry.grid(row=20,column=1)

def input_value():
    foldername=entry.get()
    return foldername

#window.grid_rowconfigure(50, weight=0)
#window.grid_columnconfigure(0, weight=0)
label1 = Label(window, text=" ")
label1.grid(row=50, column=0)
label2 = Label(window, text=" ")
label2.grid(row=60, column=0)
filepath_label = Label(window, text="Output File Path")
filepath_entry = Entry(window, width=40)
filepath_label.grid(row=100,column=0)
filepath_entry.grid(row=100,column=1)

def input_value1():
    filepath=filepath_entry.get()
    return filepath

folder_name = []
output_filepath = []
def start():
    folder_name.append(input_value())
    output_filepath.append(input_value1())
    global path
    path = str(output_filepath[0]+'/'+str(folder_name[0]))
    os.makedirs(path)
    label = Label(window, text="Select property table file")
    label.grid(row=20,column=3)


start_button = Button(master = window, text = "Start",command = start, style='W.TButton')
start_button.grid(row=20, column=2)


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
      fig.savefig(path+'/enthalpy_plot.png')
      plt.show()
def entropy_s():
      fig = plt.figure()
      plot2 = fig.add_subplot(111)
      x = df['T_val']
      s_val_pkg = df['s_val_pkg']
      s_val_CEA = df['s_val_CEA']
      plot2.plot(x, s_val_pkg, marker='o', color='green', label='s_val_pkg')
      plot2.plot(x, s_val_CEA, color='blue', label='s_val_CEA')
      plot2.set_title('Entropy (s) Validation')
      plot2.set_xlabel('Temperature, T [R]')
      plot2.set_ylabel('Entropy, s [_fill in__]')
      plot2.legend()
      fig.savefig(path+'/entropy_plot.png')
      plt.show()

def conductivity_k():
      fig = plt.figure()
      plot3 = fig.add_subplot(111)
      x = df['T_val']
      k_val_pkg = df['k_val_pkg']
      k_val_CEA = df['k_val_CEA']
      plot3.plot(x, k_val_pkg, marker='o', color='green', label='k_val_pkg')
      plot3.plot(x, k_val_CEA, color='blue', label='k_val_CEA')
      plot3.set_title('Conductivity (k) Validation')
      plot3.set_xlabel('Temperature, T [R]')
      plot3.set_ylabel('Conductivity, k [_fill in__]')
      plot3.legend()
      fig.savefig(path+'/conductivity_plot.png')
      plt.show()

def SpecHeatRat_gam():
      fig = plt.figure()
      plot4 = fig.add_subplot(111)
      x = df['T_val']
      gam_val_pkg = df['gam_val_pkg']
      gam_val_CEA = df['gam_val_CEA']
      plot4.plot(x, gam_val_pkg, marker='o', color='green', label='gam_val_pkg')
      plot4.plot(x, gam_val_CEA, color='blue', label='gam_val_CEA')
      plot4.set_title('Specific Heat Ratio (k) Validation')
      plot4.set_xlabel('Temperature, T [R]')
      plot4.set_ylabel('Specific Heat Ratio, k [none]')
      plot4.legend()
      fig.savefig(path+'/SpecHeatRat_gam__plot.png')
      plt.show()


def SpecificHeat_Cp():
      fig = plt.figure()
      plot5 = fig.add_subplot(111)
      x = df['T_val']
      Cp_val_pkg = df['Cp_val_pkg']
      Cp_val_CEA = df['Cp_val_CEA']
      plot5.plot(x, Cp_val_pkg, marker='o', color='green', label='Cp_val_pkg')
      plot5.plot(x, Cp_val_CEA, color='blue', label='Cp_val_CEA')
      plot5.set_title('Specific Heat (Cp) Validation')
      plot5.set_xlabel('Temperature, T [R]')
      plot5.set_ylabel('Specific Heat, Cp [Btu/(lbm*R)]')
      plot5.legend()
      fig.savefig(path+'/SpecificHeat_Cp_plot.png')
      plt.show()

def Viscosity_mu():
      fig = plt.figure()
      plot6 = fig.add_subplot(111)
      x = df['T_val']
      mu_val_pkg = df['mu_val_pkg']
      mu_val_CEA = df['mu_val_CEA']
      plot6.plot(x, mu_val_pkg, marker='o', color='green', label='mu_val_pkg')
      plot6.plot(x, mu_val_CEA, color='blue', label='mu_val_CEA')
      plot6.set_title('Viscosity (mu) Validation')
      plot6.set_xlabel('Temperature, T [R]')
      plot6.set_ylabel('Viscosity, mu [lbm/(ft*sec)]*10^(-5)')
      plot6.legend()
      fig.savefig(path+'/Viscosity_mu__plot.png')
      plt.show()

def GasConstant_R():
      fig = plt.figure()
      plot7 = fig.add_subplot(111)
      x = df['T_val']
      R_val_pkg = df['R_val_pkg']
      R_val_CEA = df['R_val_CEA']
      plot7.plot(x, R_val_pkg, marker='o', color='green', label='R_val_pkg')
      plot7.plot(x, R_val_CEA, color='blue', label='R_val_CEA')
      plot7.set_title('Gas Costant (R) Validation')
      plot7.set_xlabel('Temperature, T [R]')
      plot7.set_ylabel('Gas Constant, R [Btu/(lbm*R)]')
      plot7.legend()
      fig.savefig(path+'/GasConstant_R_plot.png')
      plt.show()

def Density_rho():
      fig = plt.figure()
      plot8 = fig.add_subplot(111)
      x = df['T_val']
      rho_val_pkg = df['mu_val_pkg']
      rho_val_CEA = df['mu_val_CEA']
      plot8.plot(x, rho_val_pkg, marker='o', color='green', label='rho_val_pkg')
      plot8.plot(x, rho_val_CEA, color='blue', label='rho_val_CEA')
      plot8.set_title('Density (rho) Validation')
      plot8.set_xlabel('Temperature, T [R]')
      plot8.set_ylabel('Density, rho [lbm/(ft^3)')
      plot8.legend()
      fig.savefig(path+'/Density_rho_plot.png')
      plt.show()


def getFile():
      global df
      import_file_path = filedialog.askopenfilename()
      headers = ['P_val', 'T_val', 'h_val_CEA', 's_val_CEA', 'k_val_CEA', 'mu_val_CEA', 'Cp_val_CEA', 'gam_val_CEA', 'rho_val_CEA', 'R_val_CEA', 'h_val_pkg', 's_val_pkg', 'k_val_pkg', 'mu_val_pkg', 'Cp_val_pkg', 'gam_val_pkg', 'rho_val_pkg', 'R_val_pkg', 'h_val_err', 's_val_err', 'k_val_err', 'mu_val_err', 'Cp_val_err', 'gam_val_err', 'rho_val_err', 'R_val_err', 'outlier_val']
      df = pd.read_csv(import_file_path, usecols=headers, sep=',')
      x = df['T_val']
      print(x)

browseButton = tk.Button(text='Load File...', command=getFile)
browseButton.grid(row=20, column=4)

plotButton1 = tk.Button(master=window, text='Enthalpy Validation', command=enthalpy_h, height=1, width=22)
plotButton1.grid(row=40, column=0)

plotButton2 = tk.Button(text='Entropy Validation', command=entropy_s, height=1, width=22)
plotButton2.grid(row=40, column=1)

plotButton3 = tk.Button(text='Conductivity Validation', command=conductivity_k, height=1, width=22)
plotButton3.grid(row=40, column=2)

plotButton4 = tk.Button(text='Specific Heat Ratio Validation', command=SpecHeatRat_gam, height=1, width=22)
plotButton4.grid(row=40, column=3)

plotButton5 = tk.Button(text='Specific Heat Validation', command=SpecificHeat_Cp, height=1, width=22)
plotButton5.grid(row=50, column=0)

plotButton6 = tk.Button(text='Viscosity Validation', command=Viscosity_mu, height=1, width=22)
plotButton6.grid(row=50, column=1)

plotButton7 = tk.Button(text='Gas Constant Validation', command=GasConstant_R, height=1, width=22)
plotButton7.grid(row=50, column=2)

plotButton8 = tk.Button(text='Density Validation', command=Density_rho, height=1, width=22)
plotButton8.grid(row=50, column=3)

window.mainloop()