# -*- coding: utf-8 -*-
"""
TLCD NÃO-LINEAR

"""

import math
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


def tlcd_estrutura(w, t, e_L, wa, alfa, u0, Omg_exc):
  vp = -(0.5)*(e_L)*abs(w[1])*w[1]-((2*np.pi*wa)**2)*w[0]-(alfa)*-((2*np.pi*Omg_exc)**2)*u0*np.sin(2*np.pi*Omg_exc*t)
  wp = w[1]
  return (wp, vp)

def tlcd_n_linear(tlcd_estrutura, winit, t, e_L, wa, alfa, u0, Omg_exc):
    warr = odeint(tlcd_estrutura, winit, t, args=(e_L, wa, alfa, u0, Omg_exc))
    w0 = np.sqrt(np.mean(np.square(warr[3000:5000,0])))*np.sqrt(2)
    return w0
    
#Condição inicial
n = 5000
t = np.linspace(0, 400, n)
winit = (0, 0)

#Excitação
Omg_exc = np.linspace(0, 2.5, 500)
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
