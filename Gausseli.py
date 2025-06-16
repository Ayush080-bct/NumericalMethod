import numpy as np

n=int(input("Enter no of variables: "))
A=[]
for i in range(n):
    A.append(list(map(float,input(f'Enter the Element {i+1} row with {n+1} element and Press Enter: ').split(
    ))))
A=np.array(A)
print("The augumented matrix A is: ")
print(np.matrix(A))
for i in range(n):
    pivotEl=np.argmax(np.abs(A[i:,i]))+i
    print(A[pivotEl][i])
    A[[i,pivotEl]]=A[[pivotEl,i]]
    A[i]=A[i]/A[i,i]
    print(A[i])
   # for j in range(n): 
    #    if j!=i:
     #      A[j]=A[j]-A[j,i]*A[i]
