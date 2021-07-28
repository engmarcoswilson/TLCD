# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:10:17 2021

@author: User
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
dados = pd.read_csv('TLCD_freq_x_w0_x_ceq_x_w0_linearizado.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]
ceq = dados[:,2]
ceq_gao = dados[:,3]
w0_linearizado = dados[:,4]
w0_linearizado_gao = dados[:,5]

dados2 = pd.read_csv('TLCD_freq_x_ceq_w0_constante_x_w0_linearizado.csv')
dados2 = dados2.dropna()
dados2 = dados2.to_numpy()
w0_linearizado_const = dados2[:,4]
w0_linearizado_gao_const = dados2[:,5]
Omg_exc2 = dados2[:,0]

w0_max = np.max(w0)
ind = np.argmax(w0)
w0_max_lin = np.max(w0_linearizado)
ind_lin = np.argmax(w0_linearizado)
w0_max_gao = np.max(w0_linearizado_gao)
ind_lin_gao = np.argmax(w0_linearizado_gao)
w0_max_lin_const = np.max(w0_linearizado_const)
ind_lin_const = np.argmax(w0_linearizado_const)
w0_max_gao_const = np.max(w0_linearizado_gao_const)
ind_gao_const = np.argmax(w0_linearizado_gao_const)

Omg_exc[ind] = float("{:.3f}".format(Omg_exc[ind]))
Omg_exc[ind_lin] = float("{:.3f}".format(Omg_exc[ind_lin]))
Omg_exc[ind_lin_gao] = float("{:.3f}".format(Omg_exc[ind_lin_gao]))
w0_max= float("{:.3f}".format(w0_max))
w0_max_lin= float("{:.3f}".format(w0_max_lin))
w0_max_gao= float("{:.3f}".format(w0_max_gao))
w0_max_lin_const= float("{:.3f}".format(w0_max_lin_const))
w0_max_gao_const= float("{:.3f}".format(w0_max_gao_const))
Omg_exc2[ind_lin_const] = float("{:.3f}".format(Omg_exc2[ind_lin_const]))
Omg_exc2[ind_gao_const] = float("{:.3f}".format(Omg_exc2[ind_gao_const]))


plt.figure(figsize=(14,8))
plt.plot(Omg_exc, abs(w0),label='$w_{0}$ - non-linear solution', color = 'blue')
plt.plot(Omg_exc[ind], abs(w0_max), '-o', color = 'blue')
plt.plot(Omg_exc, abs(w0_linearizado),label='$w_{0}$ - linearized solution', color = 'red')
plt.plot(Omg_exc[ind_lin], abs(w0_max_lin), '-o', color = 'red')
plt.plot(Omg_exc, abs(w0_linearizado_gao),label='$w_{0}$ - Gao linearized solution', color='green')
plt.plot(Omg_exc[ind_lin_gao], abs(w0_max_gao),'-o', color='green')
plt.plot(Omg_exc2, abs(w0_linearizado_const), '--r', label='$w_{0}$ - linearized solution - constant $w_{0}$', color='orange')
plt.plot(Omg_exc2[ind_lin_const], abs(w0_max_lin_const),'-o', color='orange')
plt.plot(Omg_exc2, abs(w0_linearizado_gao_const), '--r', label='$w_{0}$ - Gao linearized solution - constant $w_{0}$', color='purple')
plt.plot(Omg_exc2[ind_gao_const], abs(w0_max_gao_const),'-o', color='purple')
plt.text(Omg_exc[ind]-0.05, abs(w0_max)+1, (Omg_exc[ind], abs(w0_max)), color='blue')
plt.text(Omg_exc[ind_lin], abs(w0_max_lin)+8, (Omg_exc[ind_lin], abs(w0_max_lin)), color='red')
plt.text(Omg_exc[ind_lin_gao]+0.01, abs(w0_max_gao)-5, (Omg_exc[ind_lin_gao], abs(w0_max_gao)), color='green')
plt.text(Omg_exc2[ind_lin_const]-0.11, abs(w0_max_lin_const)-5, (Omg_exc2[ind_lin_const], abs(w0_max_lin_const)), color='orange')
plt.text(Omg_exc2[ind_gao_const]-0.11, abs(w0_max_gao_const)-5, (Omg_exc2[ind_gao_const], abs(w0_max_gao_const)), color='purple')
#plt.xscale("log")
plt.yscale("log")
plt.xlim(1.4, 2)
plt.ylim(1, 100)
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('w')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.savefig('TLCD_freq_x_w0', format='png')
plt.show()