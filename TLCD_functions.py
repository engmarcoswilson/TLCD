# -*- coding: utf-8 -*-
"""
TLCD Funções

"""

import math
import numpy as np
from scipy.integrate import odeint


def tlcd_estrutura(w, t, e_L, wa, alfa, u0, Omg_exc):
  vp = -(0.5)*(e_L)*abs(w[1])*w[1]-((2*np.pi*wa)**2)*w[0]-(alfa)*-((2*np.pi*Omg_exc)**2)*u0*np.cos(2*np.pi*Omg_exc*t)
  wp = w[1]
  return (wp, vp)

def tlcd_n_linear(tlcd_estrutura, winit, t, e_L, wa, alfa, u0, Omg_exc):
    warr = odeint(tlcd_estrutura, winit, t, args=(e_L, wa, alfa, u0, Omg_exc))
    w0 = np.sqrt(np.mean(np.square(warr[int(0.6*len(warr)):int(len(warr)),0])))*np.sqrt(2)
    return w0

def tlcd_linearizado_estrutura(w, t, alfa, u0, Omg_exc, ceq, rho, A, L, wa):
    vp = -(alfa)*-((2*np.pi*Omg_exc)**2)*u0*np.cos(2*np.pi*Omg_exc*t) - (ceq/(rho*A*L))*w[1]-((2*np.pi*wa)**2)*w[0]
    wp = w[1]
    return (wp, vp)


def tlcd_linearizado(tlcd_linearizado_estrutura, winit, t, alfa, u0, Omg_exc, ceq, rho, A, L, wa):
    warr = odeint(tlcd_linearizado_estrutura, winit, t, args=(alfa, u0, Omg_exc, ceq, rho, A, L, wa))
    w0 = np.sqrt(np.mean(np.square(warr[int(0.6*len(warr)):int(len(warr)),0])))*np.sqrt(2)
    return w0