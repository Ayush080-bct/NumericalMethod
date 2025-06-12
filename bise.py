# Lab1: To find a real root of a non lieanr equation by bisectioon mehtod by using python programming
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import sin, cos, exp

def f(x):
    return x**4-5*x**2+6
a,b=float(input('Enter the first integral guess:')),float(input('Enter the second integral guess'))
if f(a)*f(b)>0:
    print(f'No root lies in the interval({a},{b})')
else:
    e,N=float(input('Enter the tolerable error:')),int(input('Enter the max number of iteration:'))
    ifr=1
    A=[]
    B=[]
    while ifr<=N:
        c=(a+b)/2
        A.append([ifr,a,b,c,f(a),f(b),f(c)])
        B.append([c])
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        error=abs(b-a)

        if error<e:
            A=pd.DataFrame(A,columns=['iterations','a','b','c','f(a)','f(b)','f(c)'])
            print(f'The approx root is {(a+b)/2} in {ifr} iteration')
            print(A.to_string(index=False))
            break
        ifr+=1
    if ifr>N:
        print(f"Solution doesn't converse in {N} iteration")
x=np.linspace(-5,5,1000)
B=np.array(B)
plt.plot(x,f(x),color='r')
plt.axhline(0,0,color='black')
plt.axvline(0,0,color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title("Bisection Method")
for i,val in enumerate(B):
    plt.text(val,f(val),f'{i+1}')

plt.scatter(B,f(B))
plt.show()

