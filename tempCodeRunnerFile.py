import numpy as np
import scipy.linalg as slg #Linear algerba library
import matplotlib.pyplot as plt
import sympy as s
n=int(input("Enter the number of Data points: "))
x=np.array(list(map(float,input("Enter X-Datas: ").split())))
y=np.array(list(map(float,input("Enter Y-Datas: ").split())))
A=[[n,np.sum(x),np.sum(x**2)],
   [np.sum(x),np.sum(x**2),np.sum(x**3)],
   [np.sum(x**2),np.sum(x**3),np.sum(x**4)]
   ]
B=np.array([np.sum(y),np.sum(x*y),np.sum(x**2 * y)])
print("The matrix are: \n")
print(np.matrix(A))
print('\n')
print(np.matrix(B),'\n')
coeff=slg.solve(A,B)
print("The coffecient are",coeff)
def func(x):
    return coeff[0]+coeff[1]*x+coeff[2]*x**2
x=s.symbols("x")
f_x=coeff[0] + coeff[1]*x + coeff[2]*x**2
print("The function is",f_x)