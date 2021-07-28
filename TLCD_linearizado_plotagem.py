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

w0_max = np.max(w0)
ind = np.argmax(w0)
w0_max_lin = np.max(w0_linearizado)
ind_lin = np.argmax(w0_linearizado)
w0_max_gao = np.max(w0_linearizado_gao)
ind_lin_gao = np.argmax(w0_linearizado_gao)

Omg_exc[ind] = float("{:.3f}".format(Omg_exc[ind]))
Omg_exc[ind_lin] = float("{:.3f}".format(Omg_exc[ind_lin]))
Omg_exc[ind_lin_gao] = float("{:.3f}".format(Omg_exc[ind_lin_gao]))
w0_max= float("{:.3f}".format(w0_max))
w0_max_lin= float("{:.3f}".format(w0_max_lin))
w0_max_gao= float("{:.3f}".format(w0_max_gao))

plt.figure(figsize=(14,8))
plt.plot(Omg_exc, abs(w0),label='$w_{0}$ - non-linear solution', color = 'blue')
plt.plot(Omg_exc[ind], abs(w0_max), '-o', color = 'blue')
plt.plot(Omg_exc, abs(w0_linearizado),label='$w_{0}$ - linearized solution', color = 'red')
plt.plot(Omg_exc[ind_lin], abs(w0_max_lin), '-o', color = 'red')
plt.plot(Omg_exc, abs(w0_linearizado_gao),label='$w_{0}$ - Gao linearized solution', color='green')
plt.plot(Omg_exc[ind_lin_gao], abs(w0_max_gao),'-o', color='green')
plt.text(Omg_exc[ind]-0.05, abs(w0_max)+1, (Omg_exc[ind], abs(w0_max)), color='blue')
plt.text(Omg_exc[ind_lin], abs(w0_max_lin)+8, (Omg_exc[ind_lin], abs(w0_max_lin)), color='red')
plt.text(Omg_exc[ind_lin_gao]+0.01, abs(w0_max_gao)-5, (Omg_exc[ind_lin_gao], abs(w0_max_gao)), color='green')
#plt.xscale("log")
plt.yscale("log")
plt.xlim(1.4, 2)
plt.ylim(1, 100)
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
print(max(w0_linearizado))
print(max(w0_linearizado_gao))