# -*- coding: utf-8 -*-
"""
Simulação TLCD não-linear
Leitura arquivos csv (Omg_exc x w0)
Plotagem Omg_exc x w0
Marcos Wilson
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
dados = pd.read_csv('TLCD_freq_x_w0.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]

w0_max = np.amax(w0)
ind_max = np.argmax(w0)
w0_max = float("{:.3f}".format(w0_max))
Omg_exc[ind_max] = float("{:.3f}".format(Omg_exc[ind_max]))

plt.figure(figsize=(12,8))
plt.plot(Omg_exc, abs(w0),label='w_{0}')
plt.plot(Omg_exc[ind_max], w0_max,'-o', color='blue')
plt.text(Omg_exc[ind_max]-0.24, w0_max +3, (Omg_exc[ind_max],w0_max),fontsize=14, color='blue')
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

print(max(w0))