# -*- coding: utf-8 -*-
"""
PLOT - VIBRAÇÃO LIVRE
"""
import numpy as np
from scipy import linalg
from scipy.linalg import eigh
import matplotlib.pyplot as plt

H_vector = np.arange(0, 0.11, 0.01)

#Características da Estrutura Principal
ms = 176.935 #Kg
ks = 18330  #N/m
es = 0.01
#cc = 2*np.sqrt(ms*ks)   #Ccrítico
#cs = es*cc
cs = 36.73  #N.s/m
ws = np.sqrt(ks/ms) #Frequência Natural

#Dados do TLCD
u0 =1
rho = 1000 #Kg/m³
e_L=0.01
b = 0.0775
A = 0.0043875

def vib_livre(rho, A, H, b):
    g = 9.81
    L = 2*H+b
    alfa = b/L
    ma = rho*A*L
    mi = ma/ms
    wa = np.sqrt((2*g/L))/(2*np.pi)
    #MATRIZES DE MASSA, RIGIDEZ E AMORTECIMENTO - ESTRUTURA PRINCIPAL + ACLS
    M = [[1+mi, alfa*mi],
         [alfa*mi, mi]]

    K = [[(ws**2), 0],
         [0, (wa**2)*mi]]
    
    #IBRAÇÕES NATURAIS 
    wn2, phi = eigh(K,M)

    wn=np.sqrt(wn2)
    return wn
    
Vib_nat = np.zeros(len(H_vector))
for i in range(0, len(H_vector)):
    Vib_nat[i], phi = vib_livre(rho, A, H_vector[i], b)

plt.figure(figsize=(16,8))
plt.plot(H_vector*1000, Vib_nat, '-o')
for i in range(0, len(Vib_nat)):
    H_vector[i] = float("{:.3f}".format(H_vector[i]))
    Vib_nat[i] = float("{:.3f}".format(Vib_nat[i]))
    plt.text(H_vector[i]*1000-3, Vib_nat[i]+0.02, (H_vector[i]*1000, Vib_nat[i]))
plt.xlabel("H (mm)")
plt.ylabel('$w_{n}$ (Hz)')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.show()

    
    