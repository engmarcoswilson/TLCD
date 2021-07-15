# -*- coding: utf-8 -*-
"""
Simulação TLCD linearizado
Leitura arquivos csv (Omg_exc x w0_linearizado)
Plotagem Omg_exc x w0_linearizado
Marcos Wilson
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
dados = pd.read_csv('TLCD_freq_x_w0_x_ceq_x_w0_linearizado.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]
ceq = dados[:,2]
ceq_gao = dados[:,3]
w0_linearizado = dados[:,4]
w0_linearizado_gao = dados[:,5]

print(len(Omg_exc))

plt.figure(figsize=(12,8))
plt.plot(Omg_exc, abs(w0),label='w0')
plt.plot(Omg_exc, abs(w0_linearizado),label='w0_linearizado')
plt.plot(Omg_exc, abs(w0_linearizado_gao),label='w0_linearizado - gao')
#plt.xscale("log")
plt.yscale("log")
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('w')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.savefig('TLCD_freq_x_w0', format='png')
plt.show()



