import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#eqn=input("Enter the equation: ")
#def F(x,eqn):
   #( return eval(eqn)#it will convert the equation innto a proper solvable since eqn is only string or character
#it doest not evaluate the expression it likes writing printf("a+b") instead of a+b)
def f(x):
    return np.exp(x)+np.sin(x)-9


a=float(input("Enter the first intial guess a: "))
b=float(input("Enter the second guess b: "))
if f(a)==f(b):
    print(f'The solution is not found since {a}={b}')
else:
     e,N=float(input("Enter the toreable error: ")),int(input("Enter the max no of iterations: "))
     i=1
     table=[]
     m=[]
     while(i<=N):
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        er = abs((c-b))
        
        
        table.append([i,a,b,c,f(a),f(b),f(c),er])
        m.append(c)
        a=b
        b=c
        
        if er<e:
            break
        i+=1
    # DataFrame formatting
     pd.set_option('display.float_format', '{:.5f}'.format)  
     df= pd.DataFrame(table , columns=['Iteration', 'a', 'b', 'c (midpoint)', 'f(a)', 'f(b)', 'f(c)', 'Error'])
     print(df.to_string(index=False))  

     if er < e:
        print(f'The approximate root is {c:.6f} in {i} iterations')
     else:
        print(f'The solution did not converge in {N} iterations')
     x = np.linspace(c-10,c+10,400)
     plt.plot(x, f(x), label=r'$x^2 - 4x - 10$', color='red')  
     plt.scatter(m, f(np.array(m)), color='blue')
 
     for i, val in enumerate(m):
        plt.text(val, f(val), f'{i+1}', fontsize=9, color='black')

     plt.axhline(0, color='g')
     plt.axvline(0, color='black')
     plt.xlabel('x')
     plt.ylabel('f(x)')
     plt.title('Error Convergence in Secant Method')
     plt.grid(True)
     plt.legend()
     plt.show()
     
      

    
        
             
    