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

def tlcd_analitico(Omg_exc, wn, es):
  exc = Omg_Exc*2*np.pi
  w = exc/wn
  u = (1/np.sqrt(np.square((1-np.square(w)))+np.square(2*es*w)))
  return u

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

w_analitico = np.zeros(len(Omg_exc))
w_numerico = np.zeros(len(Omg_exc))

#Simulação
for i in range(0, n):
  w_analitico[i] = tlcd_analitico(Omg_exc[i], ws, es)
  w_numerico[i] = tlcd_n_linear(tlcd_estrutura, winit, t, e_L, wa, alfa, u0, Omg_exc[i])
  
max = np.amax(w_analitico)
ind_max = np.argmax(w_analitico)