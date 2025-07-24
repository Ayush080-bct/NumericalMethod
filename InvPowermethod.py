import numpy as np
import pandas as pd

n = int(input("Enter the order of matrix: "))
A = []
x = []

for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row: ").split())))

A = np.array(A)
print("The matrix in A:\n", np.matrix(A))


x = np.array(list(map(float, input("Enter the initial vector: ").split())))


print("The initial vector is:\n", np.matrix(x))

e = float(input("Enter tolerable error: "))
N = int(input("Enter max iterations: "))
itr = 1
old_eigen = 0
lst = []
def inv(A):
    try:
        return np.linalg.inv(A)
    except:
        print("Matrix is singular")

while itr <= N:
    y = np.dot(inv(A), x)
    max_eigen = abs(max(y, key=abs))
    for i in range(n):
        x = y / max_eigen
    err = abs(max_eigen - old_eigen)
    lst.append([itr, max_eigen] + [x[i] for i in range(n)])
    if err < e:
        lst = pd.DataFrame(lst, columns=['itr', 'max_eigen'] + [f"x{i+1}" for i in range(n)]).to_string(index=False)
        print(lst)
        break
    old_eigen = max_eigen
    itr = itr + 1

if itr > N:
    print(f"Dominant eigen value is not found in {N} iteration.")
else:
    print(f"The dominant eigen value is {max_eigen} in {itr} iterations.")
    print(f"Corresponding eigen vector is:\n", np.matrix(x))