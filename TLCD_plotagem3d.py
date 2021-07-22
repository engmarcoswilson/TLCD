# -*- coding: utf-8 -*-
"""
Plotagem Gráfico 3d
t x w0 x c
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

dados = pd.read_csv('TLCD_freq_x_w0.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]
w0_max = max(w0)

#Dados do TLCD
u0 =1
rho = 1000 #Kg/m³
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

def amortecimento(rho, A, e_L, L, w0, Omg_exc, t):
    c = 0.5*rho*A*e_L*L*abs(w0*Omg_exc*2*np.pi*np.sin(2*np.pi*Omg_exc*t))
    return c

c=np.zeros((len(Omg_exc), len(t)-1))

for i in range(0, len(Omg_exc)):
    for j in range(0, len(t)-1):
        c[i, j] = amortecimento(rho, A, e_L, L, w0[i], Omg_exc[i], t[j])

#Plotagem
fig = plt.figure()
ax = fig.gca(projection='3d')
x = Omg_exc
y = t
X, Y = np.meshgrid(x, y)
Z = 0.5*rho*A*e_L*L*abs(w0_max*X*2*np.pi*np.sin(2*np.pi*X*Y))
cset = ax.contourf(X, Y, Z) 
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('t(s)')
fig.colorbar(cset, orientation='vertical',
             label="c")
plt.show()