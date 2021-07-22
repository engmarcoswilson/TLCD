# -*- coding: utf-8 -*-
"""
Solução numérica - Força Bruta
Sistema 2GDL - Estrutura + TLCD
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from TLCD_functions import twoGdl_experimental
from TLCD_functions import forca_bruta_twoGdl
from scipy import linalg
from scipy.linalg import eigh

dados = pd.read_csv('TLCD_freq_x_w0_x_ceq_x_w0_linearizado.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
ceq = dados[:,2]
ceq_gao = dados[:,3]
ceq_min = min(ceq)
ceq_min_gao = min(ceq_gao)

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

#tempo
n = 500
t = np.linspace(0, 400, n)
winit = (0, 0)

#Condição inicial
z0_2 = [0, 0, 0, 0]

#Dados da Força
f0 = 1
F = f0 * ks   #Amplitude da força

#Simulação
f = open('2gdl_numerical_ceq_minimo.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)

H2_u_forca_bruta = np.zeros(n)
H2_w_forca_bruta = np.zeros(n)
H2_u_forca_bruta_gao = np.zeros(n)
H2_w_forca_bruta_gao = np.zeros(n)

#MATRIZES DE MASSA, RIGIDEZ E AMORTECIMENTO - ESTRUTURA PRINCIPAL + ACLS
M = [[1+mi, alfa*mi],
     [alfa*mi, mi]]

K = [[(ws**2), 0],
     [0, (wa**2)*mi]]

C = [[2*ws*es, 0], 
     [0, ceq_min]]

C_gao = [[2*ws*es, 0], 
         [0, ceq_min_gao]]

for i in range(0, len(Omg_exc)):

    H2_u_forca_bruta[i], H2_w_forca_bruta[i] = forca_bruta_twoGdl(z0_2, t, M, K, C, f0, Omg_exc[i])
    H2_u_forca_bruta_gao[i], H2_w_forca_bruta_gao[i] = forca_bruta_twoGdl(z0_2, t, M, K, C_gao, f0, Omg_exc[i])
    w.writerow([Omg_exc[i], H2_u_forca_bruta[i], H2_w_forca_bruta[i], H2_u_forca_bruta_gao[i], H2_w_forca_bruta_gao[i]])
  
print('finalizado')
