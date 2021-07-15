# -*- coding: utf-8 -*-
"""
Plotagem Gráfico 3d
t x w0 x c
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

c=np.zeros((len(Omg_exc), len(t)))

for i in range(0, len(Omg_exc)):
    c[i, :] = amortecimento(rho, A, e_L, L, w0[i], Omg_exc[i], t)
print(max(c))

# Importando as bibliotecas necessárias
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
 
# Criando a figura e projeção em 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
 
# Utilizando dados de teste
t, w0, c = axes3d.get_test_data(0.05)

# Criando o gráfico com extend3d
ax.plot_surface(w0, t, c)
ax.set_xlabel('w0')
ax.set_ylabel('t')
ax.set_zlabel('c')
ax.set_xlim(-20, 20)
ax.set_ylim(0, 60)
plt.yticks(np.arange(0, 60, 10))
# Exibindo o gráfico criado
plt.show()
