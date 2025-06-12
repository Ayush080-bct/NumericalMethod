import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return x*np.tan(x)-1
a, b = float(input('Enter two initial guesses: ')), float(input())

if (f(a) * f(b)) > 0:
    print(f'No root lies in the interval ({a}, {b})!')
else:
    e = float(input('Enter tolerable error: '))
    N = int(input('Enter max number of iterations: '))

    itr = 1
    A = []  
    m = []  

    while itr <= N:
        c = ((a*f(b)-b*f(a))/(f(b)-f(a)))  
        er = abs((b - a) / b)

        A.append([itr, a, b, c, f(a), f(b), f(c), er])  
        m.append(c)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        if er < e or abs(f(c)) < e:
             break  
        
        itr += 1

    pd.set_option('display.float_format', '{:.6f}'.format)  
    A = pd.DataFrame(A, columns=['Iteration', 'a', 'b', 'c (midpoint)', 'f(a)', 'f(b)', 'f(c)', 'Error'])
    print(A.to_string(index=False))  

    if er < e or abs(f(c))<e:
        print(f'The approximate root is {c:.6f} in {itr} iterations')
    else:
        print(f'The solution did not converge in {N} iterations')

    x = np.linspace(-5, 5, 100)
    plt.plot(x, f(x), label=r'$e^x + x$', color='red')  
    plt.scatter(m, f(np.array(m)), color='blue')

    for i, val in enumerate(m):
        plt.text(val, f(val), f'{i+1}', fontsize=9, color='black')

    plt.axhline(0, color='g')
    plt.axvline(0, color='black')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Error Convergence in Regular Falsi Method')
    plt.grid(True)
    plt.legend()
    plt.show() 