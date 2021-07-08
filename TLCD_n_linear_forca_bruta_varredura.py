# -*- coding: utf-8 -*-
"""
TLCD não-linear
Varredura harmônica por força Bruta
Plotagem gráficos t x w0 para 10 frequências
Marcos Wilson
"""

import math
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from TLCD_functions import tlcd_estrutura
from TLCD_functions import tlcd_n_linear

#Condição inicial
n = 500
t = np.linspace(0, 400, n)
winit = (0, 0)

#Excitação
Omg_exc = np.logspace(-1, 1, 500)

#Dados do TLCD
u0 =1
e_L=0
b = 2
H = 1
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))

#Varredura: Força Bruta
F_exc = np.array([])

for i in range(0, 500, 50):
  F_exc = np.append(F_exc, Omg_exc[i])

w0_n = np.zeros(len(F_exc))
  
for i in range(0, len(F_exc)):
  print('Frequência analisada:  %.3f Hz'%F_exc[i])
  warr = odeint(tlcd_estrutura, winit, t, args=(e_L, wa, alfa, u0, F_exc[i]))
  w0_n[i] = tlcd_n_linear(tlcd_estrutura, winit, t, e_L, wa, alfa, u0, F_exc[i])
  w = w0_n[i]*np.cos(F_exc[i]*2*np.pi*t)
  
  plt.figure(figsize=(16, 10))
  plt.plot(t, warr[:, 0], label='w(t)')
  plt.plot(t[int(len(t)/2):int(len(t))], w[int(len(t)/2):int(len(t))], label='w(t)')
  plt.rcParams['legend.fontsize'] = 12
  plt.legend(loc='upper right', prop={'size':16})
  plt.xlabel("t (s)")
  plt.ylabel('Amplitude')
  plt.legend(loc='best')
  plt.savefig('varredura_forca_bruta%.3f.png'%F_exc[i], format='png')
  plt.show()