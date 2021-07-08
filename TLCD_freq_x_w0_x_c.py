# -*- coding: utf-8 -*-
"""
Simulação Amortecimento TLCD
Leitura arquivos csv (Omg_exc x w0 x c)
Marcos Wilson
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
dados = pd.read_csv('TLCD_freq_x_w0.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]

#Dados do TLCD
u0 =1
rho = 10000 #N/m³
e_L=0.001
b = 2
H = 1
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))
A = 0.1

#tempo
n = 500
t = np.linspace(0, 400, n)
winit = (0, 0)

def c_TLCD(rho, A, B, L, u0, Omg_exc_rad, t, w0):
  c = (rho*A*L)*(((B/L)*(-u0*Omg_exc_rad*np.cos(Omg_exc_rad*t))-w0*Omg_exc_rad*np.cos(Omg_exc_rad*t)+(g/L)*w0*np.cos(Omg_exc_rad*t))/(w0*np.sin(Omg_exc_rad*t)))
  return c

Omg_exc_rad = Omg_exc*2*np.pi
c = np.zeros(len(t))
c = c_TLCD(rho, A, b, L, u0, Omg_exc_rad[200], t, w0[200])
print(c)

plt.figure(figsize=(12,8))
plt.plot(t, c,label='w0')
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("t")
plt.ylabel('c')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.show()