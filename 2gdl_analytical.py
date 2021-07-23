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
from scipy import linalg
from scipy.linalg import eigh

dados = pd.read_csv('TLCD_freq_x_w0_x_ceq_x_w0_linearizado.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
ceq = dados[:,2]
ceq_gao = dados[:,3]

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

#tempo
n = 500
t = np.linspace(0, 400, n)
winit = (0, 0)

#Execução da Simulação
#Estrutura Acoplada (Est. Principal + TLCD)
f = open('2gdl_analytical.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)
#Amortecimento
ea = ceq/(2*ma*wa)
ea_gao = ceq_gao/(2*ma*wa)

#Solução própria
H2_u_analiticoi = np.zeros(n, dtype='complex')
H2_w_analiticoi = np.zeros(n, dtype='complex')
H2_u_analitico = np.zeros(n)
H2_w_analitico = np.zeros(n)

#Solução - Gao
H2_u_analiticoi_gao = np.zeros(n, dtype='complex')
H2_w_analiticoi_gao = np.zeros(n, dtype='complex')
H2_u_analitico_gao = np.zeros(n)
H2_w_analitico_gao = np.zeros(n)

for i in range(0, len(Omg_exc)):
    #Solução própria
    H2_u_analiticoi[i], H2_w_analiticoi[i] = twoGdl_analitico(mi, ea[i], wa, alfa, ws, es, Omg_exc[i])
    H2_u_analitico[i] = np.sqrt(H2_u_analiticoi[i]*(H2_u_analiticoi[i].conjugate()))
    H2_w_analitico[i] = np.sqrt(H2_w_analiticoi[i]*(H2_w_analiticoi[i].conjugate()))
    #solução - Gao
    H2_u_analiticoi_gao[i], H2_w_analiticoi_gao[i] = twoGdl_analitico(mi, ea_gao[i], wa, alfa, ws, es, Omg_exc[i])
    H2_u_analitico_gao[i] = np.sqrt(H2_u_analiticoi[i]*(H2_u_analiticoi[i].conjugate()))
    H2_w_analitico_gao[i] = np.sqrt(H2_w_analiticoi[i]*(H2_w_analiticoi[i].conjugate()))
    w.writerow([Omg_exc[i], H2_u_analitico[i], H2_w_analitico[i], H2_u_analitico_gao[i], H2_w_analitico_gao[i]])
    
print('finalizado') 