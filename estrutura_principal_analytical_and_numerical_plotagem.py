# -*- coding: utf-8 -*-
"""
Solução analítica e numérica - PLOTAGEM
Sistema 1GdL - Estrutura Principal
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv('Estrutura_principal_analytical_and_numerical.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
H_analitico = dados[:,1]
H_forca_bruta = dados[:,2]

#Características da Estrutura Principal
ms = 176.935 #Kg
ks = 18330  #N/m
es = 0.01
#cc = 2*np.sqrt(ms*ks)   #Ccrítico
#cs = es*cc
cs = 36.73  #N.s/m
ws = np.sqrt(ks/ms)/(2*np.pi)  #Frequência Natural

H_max = np.amax(H_analitico)
ind_max = np.argmax(H_analitico)
H_max = float("{:.3f}".format(H_max))
Omg_exc[ind_max]= float("{:.3f}".format(Omg_exc[ind_max]))

plt.figure(figsize=(16,8))
plt.plot(Omg_exc, H_analitico,label='H - analytical')
plt.plot(Omg_exc, H_forca_bruta, 'k--', color='red', label='H - numerical')
plt.plot(Omg_exc[ind_max], H_max, '-o', color = 'blue')
plt.text(Omg_exc[ind_max]-0.15, H_max +4, (Omg_exc[ind_max],H_max),fontsize=14)
plt.yscale("log")
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('H(i$\Omega$)')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.show()