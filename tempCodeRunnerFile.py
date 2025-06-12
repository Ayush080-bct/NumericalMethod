import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def f(x):
    return x * np.log(x) / np.log(10) - 12.34

def g(x):
    return (np.log(x) + 1) / np.log(10)


x0 = float(input("Enter your guess: "))

if g(x0) == 0:
    print(f'Not possible! Try your guess again')
else:
    e, N = float(input("Enter the tolerable error: ")), int(input("Enter the max number of iterations: "))
    a = x0
    i = 1
    table = []

    while i <= N:
        b = a - (f(a) / g(a))
        er = abs((b - a) / b)
        table.append([i, a, f(a), g(a), b, f(b), er])

        a = b
        
        if er < e:
            break
        
        i += 1

    pd.set_option('display.float_format', '{:.6f}'.format)
    df = pd.DataFrame(table, columns=['Iteration', 'a', 'f(a)', "f'(a)", 'b (root)', 'f(b)', 'Error'])
    print(df.to_string(index=False))

    if er < e:
        print(f'The approximate root of the equation is {b:.6f} in {i} iterations')
    else:
        print(f'The solution does not converge in {N} iterations')

    x_vals = np.linspace(b - 10, b + 10, 400)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label=f"f(x) = xlog_{10}(x)", color="red")
    plt.axhline(0, color='black', linewidth=0.7)#used to draw horizontal
    plt.axvline(0, color='black', linewidth=0.7)#used to draw vertical line and 0 is the axis where line is drawn  ,color black and width 0.7
    plt.scatter(b, f(b), color='blue', label=f"Root at x = {b:.6f}")
    plt.title('Newton-Raphson Method - Function and Root')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
