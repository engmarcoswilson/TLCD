# -*- coding: utf-8 -*-
"""
Solução analítica e numérica
Sistema 1GdL - Estrutura Principal
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from TLCD_functions import estrutura_principal_analitico
from TLCD_functions import estrutura_principal_forca_bruta
from TLCD_functions import forca_bruta_1gdl

dados = pd.read_csv('TLCD_freq_x_w0_x_ceq_x_w0_linearizado.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]

#Tempo
n = 5000
t = np.linspace(0, 400, n)
winit = (0, 0)

#Características da Estrutura Principal
ms = 7.5  #Kg
ks = 490  #N/m
es = 0.01
cc = 2*np.sqrt(ms*ks)   #Ccrítico
cs = es*cc
ws = np.sqrt(ks/ms)  #Frequência Natural

#Condição inicial
z0 = [0, 0]   # x=0 e v=0

#Dados da Força
f0 = 1
F = f0 * ks   #Amplitude da força

#Execução da Simulação

#Estrutura Principal
f = open('Estrutura_principal_analytical_and_numerical.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)

H_analitico = np.zeros(len(Omg_exc))
H_forca_bruta = np.zeros(len(Omg_exc))


for i in range(0, len(Omg_exc)):
    H_analitico[i] = estrutura_principal_analitico(Omg_exc[i], ws, es)
    H_forca_bruta[i] = forca_bruta_1gdl(z0, t, ms, ks, cs, f0, Omg_exc[i])
    w.writerow([Omg_exc[i], H_analitico[i], H_forca_bruta[i]])
print('finalizado')