# -*- coding: utf-8 -*-
"""
Solução analítica
Sistema 2GDL - Estrutura + TLCD
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from TLCD_functions import twoGdl_analitico
from TLCD_functions import estrutura_principal_analitico

dados = pd.read_csv('TLCD_freq_x_w0_x_ceq_x_w0_linearizado.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]
ceq = dados[:,2]
ceq_gao = dados[:,3]
w0_linearizado = dados[:,4]
w0_linearizado_gao = dados[:,5]

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

#tempo
n = 500
t = np.linspace(0, 400, n)
winit = (0, 0)

#Características da Estrutura Principal
ms = 7.5  #Kg
ks = 490  #N/m
es = 0.01
cc = 2*np.sqrt(ms*ks)   #Ccrítico
cs = es*cc
ws = np.sqrt(ks/ms)  #Frequência Natural

#Execução da Simulação
#Estrutura Principal
H_analitico = np.zeros(n)
H2_u_analiticoi = np.zeros(n, dtype='complex')
H2_w_analiticoi = np.zeros(n, dtype='complex')
H2_u_analitico = np.zeros(n)
H2_w_analitico = np.zeros(n)



for i in range(0, len(Omg_exc)):
  H2_u_analiticoi[i], H2_w_analiticoi[i] = twoGdl_analitico(mi, ea, wa, alfa, ws, es, Omg_exc[i])
  H2_u_analitico[i] = np.sqrt(H2_u_analiticoi[i]*(H2_u_analiticoi[i].conjugate()))
  H2_w_analitico[i] = np.sqrt(H2_w_analiticoi[i]*(H2_w_analiticoi[i].conjugate()))