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

print(w0)

plt.figure(figsize=(12,8))
plt.plot(Omg_exc, abs(w0),label='w0')
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