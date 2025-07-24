import numpy as np
import scipy.linalg as slg  # Linear algebra library
import matplotlib.pyplot as plt
import sympy as s

# Input
n = int(input("Enter the number of Data points: "))
x_data = np.array(list(map(float, input("Enter X-Datas: ").split())))
y_data = np.array(list(map(float, input("Enter Y-Datas: ").split())))

# Matrix A for quadratic fitting
A = [
    [n, np.sum(x_data), np.sum(x_data**2)],
    [np.sum(x_data), np.sum(x_data**2), np.sum(x_data**3)],
    [np.sum(x_data**2), np.sum(x_data**3), np.sum(x_data**4)]
]
B = np.array([np.sum(y_data), np.sum(x_data * y_data), np.sum(x_data**2 * y_data)])

print("The matrix A is:\n", np.matrix(A), '\n')
print("The matrix B is:\n", np.matrix(B), '\n')

# Solve for coefficients
coeff = slg.solve(A, B)
print("The coefficients are:", coeff)

# Define the numerical function
def func(x):
    return coeff[0] + coeff[1]*x + coeff[2]*x**2

# Define symbolic variable and expression
x_sym = s.Symbol("x")
f_x = coeff[0] + coeff[1]*x_sym + coeff[2]*x_sym**2
print("The function is:", f_x)

# Plotting
x_plot = np.linspace(min(x_data), max(x_data), 100)
y_plot = func(x_plot)

plt.scatter(x_data, y_data, color='red', label='Data Points')
plt.plot(x_plot, y_plot, color='blue', label='Fitted Curve')
plt.title("Quadratic Fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
