# -*- coding: utf-8 -*-
"""
Solução Numérica - PLOTAGEM
Sistema Acoplado 2GDL - Estrutura + TLCD
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg
from scipy.linalg import eigh

#Estrutura Principal isolada - Dados
dados = pd.read_csv('Estrutura_principal_analytical_and_numerical.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
H_forca_bruta = dados[:,2]
H_max = np.amax(H_forca_bruta)
ind_max = np.argmax(H_forca_bruta)

#Estrutura Acoplada - 2 graus de liberdade - Dados
dados2 = pd.read_csv('2gdl_numerical.csv')
dados2 = dados2.dropna()
dados2 = dados2.to_numpy()

Omg_exc2 = dados2[:,0]
H2_u_forca_bruta = dados2[:,1]
H2_w_forca_bruta = dados2[:,2]

H2u_max1 = np.amax(H2_u_forca_bruta[0: int(0.1*len(H2_u_forca_bruta))])
H2u_max2 = np.amax(H2_u_forca_bruta[int(0.1*len(H2_u_forca_bruta)):int(len(H2_u_forca_bruta))])
H2w_max1 = np.amax(H2_w_forca_bruta[0: int(0.1*len(H2_w_forca_bruta))])
H2w_max2 = np.amax(H2_w_forca_bruta[int(0.1*len(H2_w_forca_bruta)):int(len(H2_w_forca_bruta))])

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
b = 3.856
H = 4
L = 2*H+b
alfa = b/L
g = 9.81
wa = np.sqrt((2*g/L))
A = 0.0000636
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

Omg_exc[ind_max] = "{:.3f}".format(Omg_exc[ind_max])
wnHz[0] = "{:.3f}".format(wnHz[0])
wnHz[1] = "{:.3f}".format(wnHz[1])
H_max = float("{:.3f}".format(H_max))
H2u_max1 = float("{:.3f}".format(H2u_max1))
H2u_max2 = float("{:.3f}".format(H2u_max2))
H2w_max1 = float("{:.3f}".format(H2w_max1))
H2w_max2 = float("{:.3f}".format(H2w_max2))


plt.figure(figsize=(16,8))
plt.plot(Omg_exc, H_forca_bruta,label='H -1GdL')
plt.plot(Omg_exc[ind_max], H_max, '-o', color='blue')
plt.text(Omg_exc[ind_max]-0.15, H_max +12, (Omg_exc[ind_max],H_max),fontsize=14, color='blue')
plt.plot(Omg_exc2, H2_u_forca_bruta, color = 'green', label='$u_{0}$')
plt.plot(Omg_exc2, H2_w_forca_bruta,color = 'orange',label='$w_{0}$')
plt.plot(wnHz[0], H2u_max1, '-o', color='green')
plt.text(wnHz[0]-0.14, H2u_max1 +1.5, (wnHz[0],H2u_max1),fontsize=14, color='green')
plt.plot(wnHz[1], H2u_max2, '-o', color='green')
plt.text(wnHz[1]-0.14, H2u_max2 + 0.2, (wnHz[1],H2u_max2),fontsize=14, color='green')
plt.plot(wnHz[0], H2w_max1, '-o', color = 'orange')
plt.text(wnHz[0]-0.14, H2w_max1 +0.1, (wnHz[0],H2w_max1),fontsize=14, color = 'orange')
plt.plot(wnHz[1], H2w_max2, '-o', color = 'orange')
plt.text(wnHz[1]-0.14, H2w_max2 +0.1, (wnHz[1],H2w_max2),fontsize=14, color = 'orange')
plt.yscale("log")
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('H(i$\Omega$)')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.show()
