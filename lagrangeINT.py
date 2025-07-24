import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
n=int(input("No of data points: "))
X=np.array(list(map(float,input("Enter all X-data: ").split())))
Y=np.array(list(map(float,input("Enter all Y-data: ").split())))
print("Data points are: ")
for i in range(n):
    print(f'{X[i]},{Y[i]}')
x=sp.symbols('x')

poly=0
for i in range(n):
    lf=1
    for j in range(n):
        if j!=i:
            lf*=(x-X[j])/(X[i]-X[j])
    poly+=Y[i]*lf
poly=sp.simplify(poly)
poly=sp.N(poly,6)
print(f'Largrane interpolation polynomial is : {poly} \n')
xp=float(input('Enter interpolation point: '))
int_val=poly.subs(x,xp)
print(f'Value of interpolation polynomial at {xp} is {int_val}')
f=sp.lambdify(x,poly,'numpy')
x_val=np.linspace(-10,10,1000)
plt.figure(figsize=(10,6))
plt.plot(x_val,f(x_val),label='Lagrange interpolation')
plt.scatter(X,Y,color='red',zorder=5,label='Data points')
plt.scatter(xp,int_val,color='green',zorder=5,label="Interpolation points")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation Polynomial')
plt.legend()
plt.grid(True)
plt.show()
