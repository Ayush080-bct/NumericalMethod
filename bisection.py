import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return x**4-5*x**2+6  # Cort function definition

# Input initial guesses
a, b = float(input('Enter two initial guesses: ')), float(input())

# Check if root lies in the interval
if (f(a) * f(b)) > 0:
    print(f'No root lies in the interval ({a}, {b})!')
else:
    e = float(input('Enter tolerable error: '))
    N = int(input('Enter max number of iterations: '))

    itr = 1
    A = []  
    m = []  

    while itr <= N:
        c = (a + b) / 2  # Midpoint calculation in each iteration
        er = abs((b - a) / b)

        A.append([itr, a, b, c, f(a), f(b), f(c), er])  # Store iteration data
        m.append(c)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        if er < e:
            break

        itr += 1

    # DataFrame formatting
    pd.set_option('display.float_format', '{:.6f}'.format)  
    A = pd.DataFrame(A, columns=['Iteration', 'a', 'b', 'c (midpoint)', 'f(a)', 'f(b)', 'f(c)', 'Error'])
    print(A.to_string(index=False))  

    # Final output
    if er < e:
        print(f'The approximate root is {c:.6f} in {itr} iterations')
    else:
        print(f'The solution did not converge in {N} iterations')

    # Plot error convergence
    x = np.linspace(-5, 5, 100)
    plt.plot(x, f(x), label=r'$x^2 - 4x - 10$', color='red')  
    plt.scatter(m, f(np.array(m)), color='blue')

    for i, val in enumerate(m):
        plt.text(val, f(val), f'{i+1}', fontsize=9, color='black')

    plt.axhline(0, color='g')
    plt.axvline(0, color='black')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Error Convergence in Bisection Method')
    plt.grid(True)
    plt.legend()
    plt.show()