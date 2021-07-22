# -*- coding: utf-8 -*-
"""
Solução numérica - PLOTAGEM
Sistema 2GDL - Estrutura + TLCD
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg
from scipy.linalg import eigh

dados = pd.read_csv('2gdl_numerical.csv')
dados = dados.dropna()
dados = dados.to_numpy()

Omg_exc = dados[:,0]
H2_u_forca_bruta = dados[:,1]
H2_w_forca_bruta = dados[:,2]
H2_u_forca_bruta_gao = dados[:,3]
H2_w_forca_bruta_gao = dados[:,4]

dados2 = pd.read_csv('2gdl_analytical.csv')
dados2 = dados2.dropna()
dados2 = dados2.to_numpy()

Omg_exc2 = dados2[:,0]
H2_u_analitico = dados2[:,1]
H2_w_analitico = dados2[:,2]
H2_u_analitico_gao = dados2[:,3]
H2_w_analitico_gao = dados2[:,4]

#Características da Estrutura Principal
ms = 7.5  #Kg
ks = 490  #N/m
es = 0.01
cc = 2*np.sqrt(ms*ks)   #Ccrítico
cs = es*cc
ws = np.sqrt(ks/ms)  #Frequência Natural

#Dados do TLCD
u0 =1
rho = 1000 #Kg/m³
e_L=0.001
b = 2
H = 1
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))
A = 0.1
ma = rho*A*L
mi = ma/ms

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
wnHz = wn/(2*np.pi)
print("\nNatural Frequencies, Hz - Estrutura principal: ", ws/(2*np.pi), 
      "\n                          Amortecedor:         ", wa/(2*np.pi),
      "\n                          Estrutura acoplada:  ", wnHz)

plt.figure(figsize=(16,8))
plt.plot(Omg_exc, H2_u_forca_bruta, color = 'blue', label='u_{0} - numerical')
plt.plot(Omg_exc, H2_w_forca_bruta,color = 'red',label='w_{0} - numerical')
plt.plot(Omg_exc2, H2_u_analitico, color = 'green', label='u_{0} - anlytical')
plt.plot(Omg_exc2, H2_w_analitico,color = 'orange',label='w_{0} - analytical')
plt.yscale("log")
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('H(i$\Omega$)')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.show()

print(max(H2_u_analitico))
print(max(H2_u_forca_bruta))