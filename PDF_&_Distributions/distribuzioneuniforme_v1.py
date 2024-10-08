# -*- coding: utf-8 -*-
"""DistribuzioneUniforme_v1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/168RJ3cCyKxriswzUCy8CzqvO6rq6WPsQ
"""

import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import norm
from scipy.stats import uniform
from scipy.optimize import curve_fit
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


#limits of the distribution
x_low=-100
x_high=100
sample=50000

np.random.seed(1)
x = [np.random.randint(x_low, x_high) for _i in range(sample)]
histo_bin=100

(loc, scale) =  uniform.fit(x)
n, bins, patches = plt.hist(x, histo_bin, density=True, facecolor = 'blue', alpha = 0.5, label='uniform distribution');

centers = (0.5*(bins[1:]+bins[:-1]))
plt.plot(centers, uniform.pdf(centers, loc, scale), 'k--',linewidth = 3, label='fit')
plt.title('Uniform Distribution --- [{:.1f},{:.1f}]'.format(x_low,x_high))

plt.legend(loc="lower right")
plt.show()