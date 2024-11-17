# -*- coding: utf-8 -*-
"""OneSampleT-Test.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dwAIg1VWbgxduvtDV5oVfLPn-dpJ8Liv

**One Sample T-Test in Python**

Very simple application of the One Sample T-Test

*   import the scipy.stats module
*   define the sample and the mean of the population
*   use the ttest_1samp function to perform the one sample t-test
*   interpret the results.
"""

import scipy.stats as stats
sample = [2, 3, 4, 5, 6, 7, 8, 9, 10]
population_mean = 5
t_statistic, p_value = stats.ttest_1samp(sample, population_mean)
if p_value < 0.05:
    print("Reject the null hypothesis. Significant differences exist between the sample mean and the population mean.")
else:
    print("Fail to reject the null hypothesis. No significant differences exist between the sample mean and the population mean.")

sample2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
population_mean = 2
t_statistic, p_value = stats.ttest_1samp(sample, population_mean)
if p_value < 0.05:
    print("Reject the null hypothesis. Significant differences exist between the sample mean and the population mean.")
else:
    print("Fail to reject the null hypothesis. No significant differences exist between the sample mean and the population mean.")