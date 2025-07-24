import numpy as np
import pandas as pd

# Input: number of equations
n = int(input("Enter the number of rows (equations): "))

# Input: Augmented matrix
A = []
for i in range(n):
    row = list(map(float, input(f"Enter the elements in row {i+1} (include {n+1} elements): ").split()))
    if len(row) != n + 1:
        raise ValueError(f"Row {i+1} must contain exactly {n+1} elements.")
    A.append(row)

# Convert to numpy array
A = np.array(A)

# Display augmented matrix
print("\nThe augmented matrix is:")
print(np.matrix(A))

# Input: tolerance and max iterations
e = float(input("Enter the tolerance error: "))
N = int(input("Enter the maximum number of iterations: "))

# Initialization
x = np.zeros(n)
table = []
itr = 1

# Gauss-Seidel Iteration
while itr <= N:
    x_old = np.copy(x)
    for i in range(n):
        s = sum(A[i][j] * x[j] for j in range(n) if j != i)
        x[i] = (A[i][-1] - s) / A[i][i]
    
    # Save current iteration result
    table.append([itr] + list(np.round(x, 6)))

    # Error check
    err = np.abs(x - x_old)
    if np.all(err < e):
        break
    itr += 1

# Output Results
df = pd.DataFrame(table, columns=["Iter"] + [f'x{i+1}' for i in range(n)])
print("\nIteration Table:")
print(df)

if itr > N:
    print(f"\nSolution did not converge in {N} iterations.")
else:
    print("\nThe solution is:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")
