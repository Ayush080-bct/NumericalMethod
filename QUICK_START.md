# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install numpy pandas matplotlib scipy sympy
```

### Step 2: Try Your First Program
```bash
python bisection.py
```

**Sample Input**:
```
Enter two initial guesses: 1
3
Enter tolerable error: 0.0001
Enter max number of iterations: 20
```

### Step 3: Understand the Output
- You'll see an iteration table showing convergence
- A graph will pop up showing the function and root approximations
- Final answer with number of iterations

---

## 📋 Quick Reference: When to Use Each Method

### Need to Find a Root? (Solve f(x) = 0)

| Method | File | Best For | Speed | Difficulty |
|--------|------|----------|-------|------------|
| Bisection | `bisection.py` | Guaranteed convergence | Slow | ⭐ Easy |
| Regula Falsi | `RegularFalsi.py` | Faster than bisection | Medium | ⭐⭐ Medium |
| Newton-Raphson | `Newrap.py` | Very fast convergence | Fast | ⭐⭐⭐ Hard |
| Secant | `secant.py` | No derivative needed | Fast | ⭐⭐ Medium |
| Fixed Point | `fixedpointiteration.py` | Simple problems | Medium | ⭐⭐ Medium |

### Need to Solve Linear Systems? (Ax = b)

| Method | File | Best For | Size Limit |
|--------|------|----------|------------|
| Gauss-Jordan | `gaussjordan.py` | Get inverse matrix | Small (< 100) |
| Gaussian | `Gausseli.py` | General purpose | Medium (< 1000) |
| Gauss-Seidel | `gausssedial.py` | Large sparse systems | Large (> 1000) |
| LU Decomposition | `lu.py` | Multiple right-hand sides | Medium |

### Need Eigenvalues?

| Method | File | Finds |
|--------|------|-------|
| Power Method | `eigen_dominant.py` | Largest eigenvalue |
| Inverse Power | `InvPowermethod.py` | Smallest eigenvalue |

### Need to Fit Data?

| Method | File | Use Case |
|--------|------|----------|
| Lagrange | `lagrangeINT.py` | Exact fit through points |
| Least Squares | `leastssquaremethod.py` | Best fit with noise |

---

## 💡 Common Input Patterns

### Root Finding Methods
```
Initial guess(es): Where you think the root is
Tolerable error: 0.0001 (smaller = more accurate but more iterations)
Max iterations: 20-100 (safety limit)
```

### Linear Systems (3x3 example)
```
Enter no of variables: 3
Enter row 1: 2 1 -1 8
Enter row 2: -3 -1 2 -11
Enter row 3: -2 1 2 -3
Enter tolerable error: 0.0001
Enter max iterations: 50
```

### Eigenvalue Problems
```
Enter order: 3
Enter row 1: 2 1 0
Enter row 2: 1 2 0
Enter row 3: 0 0 -1
Enter initial vector: 0 1 0
Enter tolerable error: 0.0001
Enter max iterations: 50
```

---

## 🎓 Study Schedule (6 Week Plan)

### Week 1: Root Finding Basics
- **Mon**: Install & run `bisection.py`
- **Tue**: Try `RegularFalsi.py`, compare with bisection
- **Wed**: Learn `Newrap.py` (Newton-Raphson)
- **Thu**: Practice with different functions
- **Fri**: Study `secant.py` and `fixedpointiteration.py`

### Week 2: Linear Systems (Direct)
- **Mon-Tue**: Master `gaussjordan.py`
- **Wed-Thu**: Learn `Gausseli.py`
- **Fri**: Understand `lu.py` decomposition

### Week 3: Linear Systems (Iterative)
- **Mon-Wed**: Learn `gausssedial.py`
- **Thu-Fri**: Compare direct vs iterative methods

### Week 4: Eigenvalues
- **Mon-Wed**: Study `eigen_dominant.py`
- **Thu-Fri**: Learn `InvPowermethod.py`

### Week 5: Interpolation
- **Mon-Wed**: Master `lagrangeINT.py`
- **Thu-Fri**: Learn `leastssquaremethod.py`

### Week 6: Practice & Projects
- **Mon-Fri**: Real-world applications and projects

---

## 🔧 Troubleshooting

### "No root lies in the interval"
- **Problem**: Your initial guesses don't bracket a root
- **Solution**: Try different values where f(a) and f(b) have opposite signs

### "Solution did not converge"
- **Problem**: Too few iterations or bad initial guess
- **Solution**: Increase max iterations or try better starting point

### "Matrix is singular"
- **Problem**: Matrix has no inverse (determinant = 0)
- **Solution**: Check your matrix entries, may need different method

### Import errors
- **Problem**: Libraries not installed
- **Solution**: `pip install numpy pandas matplotlib scipy sympy`

---

## 📝 Practice Problems

### Easy (Week 1)
1. Find root of f(x) = x² - 4 using bisection [interval: 0 to 3]
2. Find root of f(x) = x³ - x - 2 using Newton-Raphson [guess: 1.5]

### Medium (Week 2-3)
3. Solve system:
   ```
   2x + y - z = 8
   -3x - y + 2z = -11
   -2x + y + 2z = -3
   ```

### Advanced (Week 4-5)
4. Find dominant eigenvalue of:
   ```
   [4  1  0]
   [1  4  1]
   [0  1  4]
   ```

5. Fit a quadratic curve to data points: (0,1), (1,3), (2,7), (3,13)

---

## 🎯 Learning Objectives

By the end of this course, you should be able to:

- ✅ Choose the right numerical method for a problem
- ✅ Understand convergence and error analysis
- ✅ Implement basic numerical algorithms
- ✅ Interpret iteration tables and graphs
- ✅ Apply methods to real-world problems
- ✅ Debug convergence issues

---

## 📚 Additional Resources with Student Pack

Your GitHub Student Pack includes:

- **GitHub Pro**: Version control all your code
- **JetBrains Suite**: Use PyCharm Professional
- **DigitalOcean Credits**: Deploy computation servers
- **AWS Credits**: Run intensive calculations
- **Microsoft Azure**: Cloud computing resources

Access at: https://education.github.com/pack

---

## 🤝 Need Help?

1. **Check README.md**: Full detailed guide
2. **Review code comments**: Each file has inline explanations
3. **Try simpler inputs**: Start with small matrices/simple functions
4. **Compare with examples**: Use the practice problems
5. **Ask in discussions**: GitHub repository discussions

---

**Remember**: Numerical methods are about finding approximate solutions efficiently. Don't worry if you don't get exact answers - that's the point! Focus on understanding convergence and error.

Good luck with your studies! 🎉
