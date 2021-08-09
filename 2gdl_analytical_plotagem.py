# -*- coding: utf-8 -*-
"""
Solução analítica - PLOTAGEM
Sistema 2GDL - Estrutura + TLCD
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg
from scipy.linalg import eigh

dados = pd.read_csv('2gdl_analytical.csv')
dados = dados.dropna()
dados = dados.to_numpy()

Omg_exc = dados[:,0]
H2_u_analitico = dados[:,1]
H2_w_analitico = dados[:,2]
H2_u_analitico_gao = dados[:,3]
H2_w_analitico_gao = dados[:,4]

#Características da Estrutura Principal
ms = 176.935 #Kg
ks = 18330  #N/m
es = 0.01
#cc = 2*np.sqrt(ms*ks)   #Ccrítico
#cs = es*cc
cs = 36.73  #N.s/m
ws = np.sqrt(ks/ms)/(2*np.pi)  #Frequência Natural

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
ma = rho*A*L
mi = ma/ms

u_max1 = np.max(H2_u_analitico[0:int(0.66*len(Omg_exc))])
u_max2 = np.max(H2_u_analitico[int(0.665*len(Omg_exc)):len(Omg_exc)])
w_max1 = np.max(H2_w_analitico[0:int(0.66*len(Omg_exc))])
w_max2 = np.max(H2_w_analitico[int(0.665*len(Omg_exc)):len(Omg_exc)])

#MATRIZES DE MASSA, RIGIDEZ E AMORTECIMENTO - ESTRUTURA PRINCIPAL + ACLS
#Vibração livre
M = [[1+mi, alfa*mi],
     [alfa*mi, mi]]

K = [[(ws**2), 0],
     [0, (wa**2)*mi]]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#IBRAÇÕES NATURAIS 
wn2, phi = eigh(K,M)

wn=np.sqrt(wn2)
print("\nNatural Frequencies, Hz - Estrutura principal: ", ws, 
      "\n                          Amortecedor:         ", wa,
      "\n                          Estrutura acoplada:  ", wn)

wn[0] = float("{:.3f}".format(wn[0]))
wn[1] = float("{:.3f}".format(wn[1]))
u_max1 = float("{:.3f}".format(u_max1))
u_max2 = float("{:.3f}".format(u_max2))
w_max1 = float("{:.3f}".format(w_max1))
w_max2 = float("{:.3f}".format(w_max2))


plt.figure(figsize=(16,8))
plt.plot(Omg_exc, H2_u_analitico, color = 'blue', label='$u_{0}$')
plt.plot(wn[0], u_max1, '-o', color='blue')
plt.plot(wn[1], u_max2, '-o', color='blue')
plt.plot(Omg_exc, H2_w_analitico,color = 'red',label='$w_{0}$')
plt.plot(wn[0], w_max1, '-o', color='red')
plt.plot(wn[1], w_max2, '-o', color='red')
plt.text(wn[0]-0.035, u_max1+2, (wn[0], u_max1), color='blue')
plt.text(wn[1]-0.035, u_max2+2, (wn[1], u_max2), color='blue')
plt.text(wn[0]-0.035, w_max1+0.4, (wn[0], w_max1), color='red')
plt.text(wn[1]-0.035, w_max2+0.4, (wn[1], w_max2), color='red')
plt.yscale("log")
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('H(i$\Omega$)')
plt.xlim(1.4, 2)
plt.ylim(0.01, 20)
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.show()