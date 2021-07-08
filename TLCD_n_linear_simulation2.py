# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 01:24:20 2021

@author: User
"""

import math
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from TLCD_functions import tlcd_estrutura
from TLCD_functions import tlcd_n_linear
import csv

#Condição inicial
n = 5000
t = np.linspace(0, 400, n)
winit = (0, 0)

#Excitação
Omg_exc = np.logspace(0, 2.5, 500)
u0 = 1

#Dados do TLCD
u0 =1
e_L=0
b = 2
H = 1
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))

w0 = np.zeros(len(Omg_exc))

#Arquivo csv: Omg_exc x w0
f = open('TLCD_freq_x_w0', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)

#Simulação
for i in range(0, 500):
  w0[i] = tlcd_n_linear(tlcd_estrutura, winit, t, e_L, wa, alfa, u0, Omg_exc[i])
  w.writerow([Omg_exc[i], w0[i]])

 
plt.figure(figsize=(12,8))
plt.plot(Omg_exc, abs(w0), "r--",label='u - numérico')
plt.xscale("log")
plt.yscale("log")
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('u')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.savefig('TLCD_freq_x_w0', format='png')
plt.show()