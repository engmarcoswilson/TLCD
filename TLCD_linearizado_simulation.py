# -*- coding: utf-8 -*-
"""
Simulação TLCD linearizado
Gerando arquivos csv (Omg_exc x w0)
Marcos Wilson
"""

import math
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from TLCD_functions import tlcd_linearizado_estrutura
from TLCD_functions import tlcd_linearizado
import csv
import pandas as pd


#Condição inicial
n = 5000
t = np.linspace(0, 400, n)
winit = (0, 0)

u0 = 1

#Dados do TLCD
rho = 1000 #Kg/m³
e_L=0.01
b = 0.0775
H = 0.05
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))/(2*np.pi)
A = 0.0043875

dados = pd.read_csv('TLCD_freq_x_w0_x_ceq.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]
ceq = dados[:,2]
ceq_gao = dados[:,3]

print(len(Omg_exc))
w0_linearizado = np.zeros(len(Omg_exc))
w0_linearizado_gao = np.zeros(len(Omg_exc))

f = open('TLCD_freq_x_w0_x_ceq_x_w0_linearizado.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)

#Simulação
for i in range(0, len(Omg_exc)):
  w0_linearizado[i] = tlcd_linearizado(tlcd_linearizado_estrutura, winit, t, alfa, u0, Omg_exc[i], ceq[i], rho, A, L, wa)
  w0_linearizado_gao[i] = tlcd_linearizado(tlcd_linearizado_estrutura, winit, t, alfa, u0, Omg_exc[i], ceq_gao[i], rho, A, L, wa)
  w.writerow([Omg_exc[i], w0[i], ceq[i], ceq_gao[i], w0_linearizado[i], w0_linearizado_gao[i]])
print('finalizado')

