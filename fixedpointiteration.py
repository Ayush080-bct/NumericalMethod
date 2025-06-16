import numpy as np
def g(x):
    return (np.cos(x) + 3) / 2  
def f(x):
    return 2*x - np.cos(x) - 3  
x0 = float(input("Enter your initial guess: "))
e = float(input("Enter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))
print("\nFixed Point Iteration Method\n")
print("Iteration\t x\t\t g(x)\t\t Error")

for i in range(1, N+1):
    x1 = g(x0)
    error = abs(x1 - x0)
    print(f"{i}\t\t {x0:.6f}\t {x1:.6f}\t {error:.6f}")
    
    if error < e:
        print(f"\nConverged to root: {x1:.6f} in {i} iterations")
        break
    x0 = x1
else:
    print("\nDid not converge in the given number of iterations.")
