import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')


# label_dictionary = {}
# label_dictionary['T_val']= 'Temperature'
# label_dictionary['h_val']= 'enthalpy'


file_path = input('Enter data filepath: ')
headers = ['P_val', 'T_val', 'h_val_CEA', 's_val_CEA', 'k_val_CEA', 'mu_val_CEA', 'Cp_val_CEA', 'gam_val_CEA', 'rho_val_CEA', 'R_val_CEA', 'h_val_pkg', 's_val_pkg', 'k_val_pkg', 'mu_val_pkg', 'Cp_val_pkg', 'gam_val_pkg', 'rho_val_pkg', 'R_val_pkg', 'h_val_err', 's_val_err', 'k_val_err', 'mu_val_err', 'Cp_val_err', 'gam_val_err', 'rho_val_err', 'R_val_err', 'outlier_val']
data = pd.read_csv(file_path, usecols=headers, sep=',')

def twodplot1(xdata,  ydata, data=data, colors = ['b', 'g', 'r', 'k'], markers=['.', 'o', 'x']):
    #data = input()
    for i in range(len(ydata)):
        plot = plt.plot(data[xdata[0]],
                        data[ydata[i]],
                        label = ydata[i],
                        color = colors[i],
                        marker=markers[i])
        plt.xlabel(xdata[0])
        plt.ylabel(ydata[i])
    plt.legend()
    plt.show()
    return plot

#twodplot1(df, ['T_val'], ['h_val_pkg', 'h_val_CEA'])
