# -*- coding: utf-8 -*-
"""BaysianUpperLimit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FfAXs4l27_L9yaE_hi9tDxmn6aeq1B5b

**Simple code to evaluate the Baysian Upper Limit for a Poisson variable n and for a value of alpha =0.1**
"""

import numpy as np
from scipy.stats import gamma
from scipy import stats

def upper_limits(alpha,n,b):
  """Baysian Poisson Upper limit
1-alpha: confidence level
n: observed counts
b: background """

  return gamma.ppf(1.-alpha,(n+1))-b

def upper_limits_Chi2(alpha,n,b):
  """Baysian Poisson Upper limit
1-alpha: confidence level
n: observed counts
b: background """

  return 1/2*stats.chi2.ppf(1.-alpha,2*(n+1))-b


print(r'n b  s_up  s_up_Chi2')
print("____________________")

alpha=0.1
for n in range(10):
  print(f"{n} {0}  {upper_limits(alpha,n,0):.2f}  {upper_limits_Chi2(alpha,n,0):.2f}")
