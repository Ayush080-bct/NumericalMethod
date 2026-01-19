#!/usr/bin/env python3
"""
Example: Getting Started with Numerical Methods

This script demonstrates a simple use case of the bisection method
to help you understand how the programs work.

Author: Study Guide
Purpose: Educational example for students
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    """
    Example function: f(x) = x^2 - 4
    This has roots at x = 2 and x = -2
    """
    return x**2 - 4

def bisection_example():
    """
    Demonstrate the bisection method to find the positive root of x^2 - 4 = 0
    """
    print("=" * 60)
    print("BISECTION METHOD EXAMPLE")
    print("=" * 60)
    print("\nFinding root of f(x) = x^2 - 4")
    print("We know the roots are x = 2 and x = -2")
    print("Let's find the positive root (x = 2) using bisection.\n")
    
    # Initial setup
    a, b = 0.0, 3.0  # Interval [0, 3] brackets the root at x=2
    e = 0.0001  # Tolerance
    N = 20  # Max iterations
    
    print(f"Initial interval: [{a}, {b}]")
    print(f"f({a}) = {f(a)}")
    print(f"f({b}) = {f(b)}")
    print(f"Tolerance: {e}")
    print(f"Max iterations: {N}\n")
    
    # Check if root exists in interval
    if (f(a) * f(b)) > 0:
        print(f'No root lies in the interval ({a}, {b})!')
        return
    
    # Bisection iteration
    itr = 1
    A = []  
    m = []  
    
    print("-" * 60)
    print("Starting iterations...\n")
    
    while itr <= N:
        c = (a + b) / 2  # Midpoint
        er = abs((b - a) / b)  # Relative error
        
        A.append([itr, a, b, c, f(a), f(b), f(c), er])
        m.append(c)
        
        # Update interval
        if f(a) * f(c) < 0:
            b = c  # Root is in [a, c]
        else:
            a = c  # Root is in [c, b]
        
        # Check convergence
        if er < e:
            break
        
        itr += 1
    
    # Display results
    df = pd.DataFrame(A, columns=['Iter', 'a', 'b', 'c (midpoint)', 'f(a)', 'f(b)', 'f(c)', 'Error'])
    with pd.option_context('display.float_format', '{:.6f}'.format):
        print(df.to_string(index=False))
    
    print("\n" + "=" * 60)
    if er < e:
        print(f'✓ SUCCESS: Root found = {c:.6f} in {itr} iterations')
        print(f'  Expected root = 2.0')
        print(f'  Error from true value = {abs(c - 2.0):.6f}')
    else:
        print(f'✗ Did not converge in {N} iterations')
    print("=" * 60)
    
    # Plot the function
    x = np.linspace(-1, 4, 100)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), 'b-', label=r'$f(x) = x^2 - 4$', linewidth=2)
    plt.scatter(m, [f(val) for val in m], color='red', s=50, zorder=5, label='Iteration points')
    
    # Annotate iterations
    for i, val in enumerate(m[:5]):  # Show first 5 iterations
        plt.annotate(f'{i+1}', (val, f(val)), 
                    textcoords="offset points", xytext=(0,10), ha='center')
    
    # Plot root
    plt.scatter([c], [f(c)], color='green', s=200, marker='*', 
               zorder=6, label=f'Root ≈ {c:.4f}')
    
    # Styling
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title('Bisection Method: Finding Root of $f(x) = x^2 - 4$', fontsize=14)
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    print("\n📊 Displaying convergence graph...")
    print("   Close the graph window to exit.\n")
    plt.show()

def main():
    """Main function"""
    print("\n" + "🎓 NUMERICAL METHODS - QUICK EXAMPLE" + "\n")
    print("This example shows how the bisection method works.")
    print("After understanding this, try running the other programs!\n")
    
    input("Press Enter to start the example...")
    print()
    
    bisection_example()
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. Try modifying the function f(x) above")
    print("2. Run: python bisection.py (for interactive version)")
    print("3. Read README.md for full study guide")
    print("4. Check QUICK_START.md for more examples")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()

