# -*- coding: utf-8 -*-
"""
Simulação TLCD não-linear
Gerando arquivos csv (Omg_exc x w0)
Marcos Wilson
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
Omg_exc = np.linspace(0, 3, 500)
u0 = 1

#Dados do TLCD
e_L=0.01
b = 0.0775
H = 0.05
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))/(2*np.pi)

w0 = np.zeros(len(Omg_exc))

#Arquivo csv: Omg_exc x w0
f = open('TLCD_freq_x_w0.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)

#Simulação
for i in range(0, 500):
  w0[i] = tlcd_n_linear(tlcd_estrutura, winit, t, e_L, wa, alfa, u0, Omg_exc[i])
  w.writerow([Omg_exc[i], w0[i]])
print('finalizado')
