import numpy as np
from scipy.linalg import lu,lu_factor,lu_solve
n=int(input("Enter the number of row: "))
a=[]
b=[]
for i in range(n):
    a.append(list(map(float,input(f"Enter the element in {i+1} row {n} elements: ").split())))

a=np.array(a)
for i in range(n):
      b.append(list(map(float,input(f"Enter The constant of  eqn {i+1}: ").split())))
       
b=np.array(b)
P,L,U=lu(a)
lum=lu_factor(a)
print("Upper traingular matrix is U:\n ",U)
print("Lower traingular matrxi L : \n",L)
print("permutation matrix P: \n",P)
x=lu_solve(lum,b)
print("the solution: \n",x)