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
rho = 1000 #Kg/m³
e_L=0.01
b = 0.0775
H = 0.05
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))/(2*np.pi)
A = 0.0043875

#tempo
n = 5000
t = np.linspace(0, 400, n)
winit = (0, 0)

def c_TLCD(rho, A, B, L, e_L, Omg_exc, t, w0):
  c = (Omg_exc*w0*rho*A*(e_L*L))/np.pi
  return c

def c_gao_TLCD(rho, A, B, L, e_L, Omg_exc, t, w0):
  c = (4/3)*((Omg_exc*w0*rho*A*(e_L*L))/np.pi)
  return c


Omg_exc_rad = Omg_exc*2*np.pi
ceq = np.zeros(len(Omg_exc))
ceq_gao = np.zeros(len(Omg_exc))

for i in range(0, len(Omg_exc)):
    ceq[i] = c_TLCD(rho, A, b, L, e_L, Omg_exc[i], t, w0[i])
    ceq_gao[i] = c_gao_TLCD(rho, A, b, L, e_L, Omg_exc[i], t, w0[i])

plt.figure(figsize=(12,8))
plt.plot(Omg_exc, ceq, label='ceq')
plt.plot(Omg_exc, ceq_gao, label='ceq_gao')
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('c')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.show()

f = open('TLCD_freq_x_w0_x_ceq.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)


#Simulação
for i in range(0, len(Omg_exc)):
  w.writerow([Omg_exc[i], w0[i], ceq[i], ceq_gao[i]])
print('finalizado')
