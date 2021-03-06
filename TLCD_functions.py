# -*- coding: utf-8 -*-
"""
TLCD Funções

"""

import math
import numpy as np
from scipy.integrate import odeint


#TLCD isolado
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

#Estrutura Principal
def estrutura_principal_analitico(Omg_exc, wn, es):
    w = (Omg_exc)/wn
    H = (1/np.sqrt(np.square((1-np.square(w)))+np.square(2*es*w)))
    return H

def estrutura_principal_forca_bruta(z, t, m, k, c, f0, Omg_exc):
  x = z[0]
  v = z[1]
  dxdt = v
  dvdt = -(c/m)*v - (k/m)*x + (1/m)*(f0*k*np.cos(Omg_exc*2*np.pi*t))  #f = f0*cos(Omg_exc*t)
  dzdt = [dxdt, dvdt]
  return dzdt

def forca_bruta_1gdl(z0, t, ms, ks, cs, f0, Omg_exc):
  #Z - u (movimento da estrutura)
  z = odeint(estrutura_principal_forca_bruta, z0, t, args=(ms, ks, cs, f0, Omg_exc))
  #RMS
  u0 = np.sqrt(np.mean(np.square(z[int(len(t)/3):int(len(t)),0])))*np.sqrt(2)
  return u0

#Estrutura 2 Graus de Liberdade (Est. Principal + TLCD)
def twoGdl_analitico(mi, ea, wa, alfa, ws, es, Omg_exc):
  Omg_exc= Omg_exc*2*np.pi
  A1 = complex(-mi,0)
  A2 = complex(0, 2*mi*ea*wa)
  A3 = complex(mi*(wa**2),0)
  A4 = complex(-alfa*mi,0)
  B0 = complex((ws**2)*mi*(wa**2),0)
  B1 = complex(0, 2*mi*es*(wa**2)*ws+2*mi*ea*wa*(ws**2))
  B2 = complex((ws**2)*mi+(1+mi)*mi*(wa**2)+4*es*ws*mi*ea*wa,0)
  B3 = complex(0, (1+mi)*2*mi*ea*wa+2*es*ws*mi)
  B4 = complex((1+mi)*mi-(alfa**2)*(mi**2),0)

  Hu = ((-A1*complex((Omg_exc**2),0)+A2*complex(Omg_exc,0)+A3)/(B4*complex((Omg_exc**4),0)-B3*complex((Omg_exc**3),0)-B2*complex((Omg_exc**2),0)+B1*complex(Omg_exc,0)+B0))
  Hw = (-A4*complex((Omg_exc**2),0)/(B4*complex((Omg_exc**4),0)-B3*complex((Omg_exc**3),0)-B2*complex((Omg_exc**2),0)+B1*complex(Omg_exc,0)+B0))
  return Hu, Hw

def twoGdl_experimental(z0, t, M, K, C, f0, Omg_exc):
  x = z0[0:int(len(z0)/2)]
  y = z0[int(len(z0)/2):len(z0)]
  x1 = np.zeros((int(len(z0)/2),1))
  y1 = np.zeros((int(len(z0)/2),1))
  P = np.zeros((int(len(z0)/2),1))
  P[0, 0] = (f0*np.cos(Omg_exc*2*np.pi*t))
  P[1, 0] = 0
  for i in range (0, int(len(z0)/2)):
    x1[i,0] = x[i]
    y1[i,0] = y[i]
  Minv = np.linalg.inv(M)
  dxdt = y1
  dydt = Minv @ (- (C @ y1) - (K @ x1) + (P))
  dzdt = np.vstack((dxdt, dydt))
  dz1dt = np.zeros(len(z0))
  for j in range(0, len(z0)):
    dz1dt[j] = dzdt[j,0]
  return dz1dt

def forca_bruta_twoGdl(z0, t, M, K, C, f0, Omg_exc):
  #Z - u (movimento da estrutura)
  z = odeint(twoGdl_experimental, z0, t, args=(M, K, C, f0, Omg_exc))
  z1 = z[:,0]
  z2 = z[:,1]
  #RMS
  u0 = np.sqrt(np.mean(np.square(z1[int(len(t)/3):int(len(t))])))*np.sqrt(2)
  w0 = np.sqrt(np.mean(np.square(z2[int(len(t)/3):int(len(t))])))*np.sqrt(2)
  return u0, w0