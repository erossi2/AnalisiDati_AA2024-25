# -*- coding: utf-8 -*-
"""SimpleTwoSampleTest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LdBFvp6mAU6WR1S-c4A7ziuvi6lhUs8P
"""

# Import library
import scipy.stats as stats
import numpy as np

# Creating data groups
data_group1 = np.array([14, 15, 15, 16, 13, 8, 14, 17, 16, 14, 19, 20, 21, 15, 15, 16, 16, 13, 14, 12])

data_group2 = np.array([15, 17, 14, 17, 14, 8, 12, 19, 19, 14, 17, 22, 24, 16,13, 16, 13, 18, 15, 13])

# Print the variance of both data groups
print("group1 variance: ",np.var(data_group1),"group2 variance: ", np.var(data_group2))

# Perform the two sample t-test with equal variances
t_statistic, p_value = stats.ttest_ind(a=data_group1, b=data_group2, equal_var=True)
print("t_statistic = ",t_statistic, "p_value = ",p_value)


if p_value < 0.05:
    print("We reject the null hypothesis")
else:
    print("We accept the null hypothesis")