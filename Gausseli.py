
import numpy as np

n = int(input("Enter no of variables: "))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Enter the Element {i+1} row with {n+1} element and Press Enter: ").split())))
A = np.array(A, float)

print("\nThe Augmented Matrix is:")
print(np.matrix(A))


for i in range(n):
    
    pivot = np.argmax(np.abs(A[i:, i])) + i

    A[[i, pivot]] = A[[pivot, i]] 

  
    for j in range(i + 1, n):
       
        A[j, i:] = A[j, i:] - A[j,i]/A[i,i] * A[i, i:]

print("\nUpper Triangular Matrix is:")
print(np.matrix(A))

x = np.zeros(n)
for i in range(n-1,-1,-1):

    x[i]=(A[i,-1]-np.sum(A[i,i+1:n]*x[i+1:n]))/A[i,i]
  

print("\nThe solution is:")
print(np.matrix(x))
