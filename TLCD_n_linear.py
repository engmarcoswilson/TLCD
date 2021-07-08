# -*- coding: utf-8 -*-
"""
TLCD NÃO-LINEAR

"""

import math
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt



def tlcd(w, t, e_L, wa, alfa, u0, Omg_exc):
  vp = -(0.5)*(e_L)*abs(w[1])*w[1]-((2*np.pi*wa)**2)*w[0]-(alfa)*-((2*np.pi*Omg_exc)**2)*u0*np.sin(2*np.pi*Omg_exc*t)
  wp = w[1]
  return (wp, vp)

n = 5000
t = np.linspace(0, 100, n)
winit = (0, 0)

#Dados do TLCD
u0 =1
e_L=0
b = 2
H = 1
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L)) 

u0 = 1
warr = odeint(tlcd, winit, t, args=(e_L, wa, alfa, u0, Omg_exc))

plt.figure(figsize=(16, 10))
plt.plot(t, warr[:, 0], label='w(t)')
plt.xlabel("t (s)")
plt.ylabel('Amplitude')
plt.legend(loc='best')
plt.show()

w0 = np.sqrt(np.mean(np.square(warr[3000:5000,0])))*np.sqrt(2)
print(w0)

w_teo=w0*np.cos(Omg_exc*2*np.pi*t)

plt.figure(figsize=(16, 10))
plt.plot(t, warr[:, 0], label='w(t)')
plt.plot(t, w_teo, label="w(t) - RMS")
plt.xlabel("t (s)")
plt.rcParams['legend.fontsize'] = 12
plt.legend(loc='upper right', prop={'size':16})
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.ylabel('Amplitude')
plt.legend(loc='best')
plt.grid()
plt.show()