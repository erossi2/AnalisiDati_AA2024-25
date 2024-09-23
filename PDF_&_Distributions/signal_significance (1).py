# -*- coding: utf-8 -*-
"""Signal_significance.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tTlSLLzH1RYB3bISHbdaGSrnGF2dd3Qw
"""

import numpy as np
import matplotlib.pyplot as plt
# s/ sqrt (S+B) = n sigma
# max number of signal events

for n in range(3,6):
    f = lambda x: (n*n+np.sqrt(n*n+4*n*x))/2
    xi=0
    xf=500
    point=100
    x = np.linspace(xi,xf,point)
    y= f(x)
    plt.plot(x,y,label="S= "+str(n)+"$ \sigma$ ")
    plt.xlabel("B")
    plt.ylabel("S")
    plt.title("S/sqrt(S+B)")
    n=n+1
    plt.legend()

plt.plot([xi,xf], [nSig_max,nSig_max], linestyle='dotted')
plt.show()

nSig_max=50
for n in range(3,6):
    finv = lambda sig: (((sig**2)/n**2)-sig)
    sig_i=0
    sig_f=100
    point=100
    sig = np.linspace(sig_i,sig_f,point)
    BKG = finv(sig)
    plt.plot(sig ,BKG,label=str(n)+"$ \sigma$ ")
    plt.xlabel("S")
    plt.ylabel("B")
    plt.title("$B=S^2/n^2 -S$")

    BKG = finv(nSig_max)
    print("BKG - B = "+str(BKG)+ " for Signal S= "+str(nSig_max)+ " and n= "+str(n))
    n=n+1
    plt.legend()

plt.xticks(np.arange(0,100,10))
plt.yticks(np.arange(0,1000,100))
plt.plot( [nSig_max,nSig_max], [0,1000], linestyle='dotted')
plt.show()