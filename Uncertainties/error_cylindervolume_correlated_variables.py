# -*- coding: utf-8 -*-
"""Error_CylinderVolume_correlated_variables.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IwgXsFu3mYcHabeoPmtpppZEWL5csY6M

# ** Error Propagation for Correlated Variables **

Show usage for a simple example: Volume of a cylinder with radius r
 and height h
"""

from sympy import *
from IPython.display import display, Latex

"""SymPy is a Python library for symbolic mathematics: [SymPy](https://docs.sympy.org/latest/index.html)
With a special package for Physics: [Physics](https://docs.sympy.org/latest/guides/physics/index.html)
and also a module to solve equations: [solve equations](https://docs.sympy.org/latest/guides/solving/index.html)
"""

def gaussian_error_propagation_corr(f, x, V):
    """
    f: function f = f(x[0], x[1], ...)
    x: list of variables
    V: covariance matrix (python 2d list)
    """
    sum = sympify("0") # empty sympy expression
    for i in range(len(x)):
        for j in range(len(x)):
            sum += diff(f, x[i]) * diff(f, x[j]) * V[i][j]
    return sqrt(simplify(sum))

r, h, sigma_r, sigma_h = symbols('r, h, sigma_r, sigma_h', positive=True)
rho = Symbol("rho", real=True) # correlation coefficient
V = pi * r**2 * h # volume of a cylinder

vars = [r, h]
cov_matrix = [[sigma_r**2, rho * sigma_r * sigma_h],
              [rho * sigma_r * sigma_h, sigma_h**2]]
Matrix(cov_matrix)

sigma_V = gaussian_error_propagation_corr(V, vars, cov_matrix)
display(Latex(f"$V = {latex(V)}, \, \sigma_V = {latex(sigma_V)}$"))

"""Plug in some numbers and print the calculated volume with its uncertaity:"""

r_meas = 10 # cm
sigma_r_meas = 0.01 # cm
h_meas = 20 # cm
sigma_h_meas = 0.1 # cm

central_value = V.subs([(r,r_meas), (h, h_meas)]).evalf()
sigma = sigma_V.subs([(r, r_meas), (sigma_r, sigma_r_meas), (h, h_meas), (sigma_h, sigma_h_meas)]).evalf()

for rho_value in [-1, 0, 1]:
    sigma = sigma_V.subs([(r, r_meas), (sigma_r, sigma_r_meas), (h, h_meas), (sigma_h, sigma_h_meas), (rho, rho_value)]).evalf()
    display(Latex(f"$$ \\rho = {rho_value}: V = ({central_value:0.1f} \pm {sigma:.1f}) \, \mathrm{{cm}}^3$$"))