# Numerical Methods - Study Guide

Welcome to the Numerical Methods repository! This collection contains Python implementations of various numerical analysis algorithms commonly taught in undergraduate engineering and mathematics courses.

## 📚 Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Methods Organized by Category](#methods-organized-by-category)
- [How to Study](#how-to-study)
- [Detailed Method Descriptions](#detailed-method-descriptions)
- [Running the Programs](#running-the-programs)
- [Learning Resources](#learning-resources)

---

## Prerequisites

Before diving into numerical methods, you should have:

- **Mathematics**: 
  - Calculus (derivatives, integrals)
  - Linear Algebra (matrices, vectors, eigenvalues)
  - Basic understanding of functions and equations

- **Programming**:
  - Basic Python knowledge
  - Familiarity with loops, conditionals, and functions

- **Software**:
  - Python 3.x installed
  - Required libraries: NumPy, Pandas, Matplotlib, SciPy, SymPy

---

## Installation

1. **Clone this repository** (if you haven't already):
   ```bash
   git clone https://github.com/Ayush080-bct/NumericalMethod.git
   cd NumericalMethod
   ```

2. **Install required dependencies**:
   ```bash
   pip install numpy pandas matplotlib scipy sympy
   ```

3. **Verify installation**:
   ```bash
   python -c "import numpy, pandas, matplotlib, scipy, sympy; print('All libraries installed!')"
   ```

---

## Methods Organized by Category

### 🔍 Root Finding Methods
Methods to find solutions (roots) of equations f(x) = 0

1. **bisection.py** - Bisection Method
2. **RegularFalsi.py** - Regula Falsi (False Position) Method
3. **Newrap.py** - Newton-Raphson Method
4. **secant.py** - Secant Method
5. **fixedpointiteration.py** - Fixed Point Iteration

### 📐 Linear System Solvers
Methods to solve systems of linear equations (Ax = b)

6. **gaussjordan.py** - Gauss-Jordan Elimination
7. **Gausseli.py** - Gaussian Elimination
8. **gausssedial.py** - Gauss-Seidel Iterative Method
9. **lu.py** - LU Decomposition

### 🔢 Eigenvalue Problems
Methods to find eigenvalues and eigenvectors of matrices

10. **eigen_dominant.py** - Power Method (Dominant Eigenvalue)
11. **InvPowermethod.py** - Inverse Power Method (Smallest Eigenvalue)

### 📊 Interpolation & Curve Fitting
Methods to approximate functions from data points

12. **lagrangeINT.py** - Lagrange Interpolation
13. **leastssquaremethod.py** - Least Squares Method (Curve Fitting)

---

## How to Study

### 🎯 Recommended Learning Path

#### Week 1-2: Root Finding Methods
**Start Simple → Build Complexity**

1. **Day 1-2: Bisection Method**
   - Theory: Simplest root-finding method using interval halving
   - Run: `python bisection.py`
   - Practice: Try f(x) = x² - 4 with interval [0, 3]
   - Why it works: Based on Intermediate Value Theorem

2. **Day 3-4: Regula Falsi**
   - Theory: Improved bisection using linear interpolation
   - Run: `python RegularFalsi.py`
   - Compare: How is it faster than bisection?

3. **Day 5-6: Newton-Raphson**
   - Theory: Uses derivative for faster convergence
   - Run: `python Newrap.py`
   - Challenge: Find roots of x³ - 2x - 5 = 0

4. **Day 7-8: Secant & Fixed Point**
   - Run: `python secant.py` and `python fixedpointiteration.py`
   - Compare: Which method converges fastest?

#### Week 3-4: Linear Systems

5. **Day 9-11: Direct Methods**
   - Start with: `python gaussjordan.py`
   - Then: `python Gausseli.py`
   - Advanced: `python lu.py`
   - Practice: Solve 3x3 systems, then try 4x4

6. **Day 12-14: Iterative Methods**
   - Run: `python gausssedial.py`
   - Compare: When to use iterative vs direct methods?

#### Week 5: Eigenvalues

7. **Day 15-17: Eigenvalue Problems**
   - Run: `python eigen_dominant.py`
   - Then: `python InvPowermethod.py`
   - Application: Understand Google's PageRank algorithm

#### Week 6: Interpolation

8. **Day 18-21: Data Fitting**
   - Run: `python lagrangeINT.py`
   - Then: `python leastssquaremethod.py`
   - Project: Fit real-world data (temperature, stock prices)

---

## Detailed Method Descriptions

### 1. Bisection Method (`bisection.py`)
**What it does**: Finds roots by repeatedly halving an interval where the function changes sign.

**When to use**: 
- Simple and guaranteed to converge
- Good for initial approximation
- Slow but robust

**Example**:
```bash
python bisection.py
# Input: Two guesses where f(a) and f(b) have opposite signs
# Example: a=1, b=3, error=0.0001, max iterations=20
```

**Key Concept**: If f(a) < 0 and f(b) > 0, there must be a root between a and b.

---

### 2. Regula Falsi Method (`RegularFalsi.py`)
**What it does**: Similar to bisection but uses linear interpolation for faster convergence.

**When to use**:
- When you want faster convergence than bisection
- Function is approximately linear in the interval

**Formula**: c = (a·f(b) - b·f(a)) / (f(b) - f(a))

---

### 3. Newton-Raphson Method (`Newrap.py`)
**What it does**: Uses tangent line approximation to find roots quickly.

**When to use**:
- Very fast convergence (quadratic)
- When derivative is easy to compute
- Good initial guess available

**Formula**: x_{n+1} = x_n - f(x_n)/f'(x_n)

**Warning**: May not converge if initial guess is poor or derivative is zero.

---

### 4. Secant Method (`secant.py`)
**What it does**: Similar to Newton-Raphson but approximates derivative numerically.

**When to use**:
- Derivative is hard to compute
- Faster than bisection, no derivative needed

**Advantage**: No need for analytical derivative calculation.

---

### 5. Fixed Point Iteration (`fixedpointiteration.py`)
**What it does**: Rearranges f(x) = 0 to x = g(x) and iterates x_{n+1} = g(x_n).

**When to use**:
- Simple iterative approach
- Works when |g'(x)| < 1 near the root

---

### 6. Gauss-Jordan Elimination (`gaussjordan.py`)
**What it does**: Solves Ax = b by converting A to identity matrix.

**When to use**:
- Need the inverse of a matrix
- Small to medium-sized systems (< 1000 equations)

**Process**: Augmented matrix → Row operations → Diagonal matrix → Solution

---

### 7. Gaussian Elimination (`Gausseli.py`)
**What it does**: Solves Ax = b using forward elimination and back substitution.

**When to use**:
- Standard method for linear systems
- More efficient than Gauss-Jordan

**Process**: Create upper triangular matrix → Back substitution

---

### 8. Gauss-Seidel Method (`gausssedial.py`)
**What it does**: Iterative method that uses most recent values immediately.

**When to use**:
- Large sparse systems
- Matrix is diagonally dominant
- Iterative refinement needed

**Advantage**: Uses less memory than direct methods for large systems.

---

### 9. LU Decomposition (`lu.py`)
**What it does**: Factors matrix A into Lower (L) and Upper (U) triangular matrices.

**When to use**:
- Solving multiple systems with same A
- Computing determinants
- Matrix inversion

**Formula**: A = PLU (with permutation matrix P)

---

### 10. Power Method (`eigen_dominant.py`)
**What it does**: Finds the largest eigenvalue and corresponding eigenvector.

**When to use**:
- Finding dominant eigenvalue
- Applications in stability analysis, Google PageRank

**Process**: Repeatedly multiply matrix by vector → Normalize → Converge to dominant eigenvector

---

### 11. Inverse Power Method (`InvPowermethod.py`)
**What it does**: Finds the smallest eigenvalue by applying power method to A⁻¹.

**When to use**:
- Finding smallest eigenvalue
- Stability analysis

---

### 12. Lagrange Interpolation (`lagrangeINT.py`)
**What it does**: Constructs polynomial passing through all data points.

**When to use**:
- Exact fit to data points
- Small number of points (< 10)

**Warning**: May oscillate wildly with many points (Runge's phenomenon).

---

### 13. Least Squares Method (`leastssquaremethod.py`)
**What it does**: Fits best curve (quadratic) minimizing squared errors.

**When to use**:
- Data has noise/errors
- Need smooth approximation
- Regression analysis

**Application**: Weather prediction, trend analysis, machine learning

---

## Running the Programs

### General Steps for All Programs:

1. **Navigate to the directory**:
   ```bash
   cd /path/to/NumericalMethod
   ```

2. **Run a program**:
   ```bash
   python <filename.py>
   ```

3. **Provide inputs** when prompted:
   - Initial guesses
   - Tolerance/error
   - Maximum iterations
   - Matrix elements (for linear systems)

4. **Observe outputs**:
   - Iteration tables (Pandas DataFrame)
   - Approximate solution
   - Convergence graphs (Matplotlib)

### Example Session:

```bash
$ python bisection.py
Enter two initial guesses: 1
3
Enter tolerable error: 0.0001
Enter max number of iterations: 20

# Program shows iteration table and plots graph
The approximate root is 2.000000 in 15 iterations
```

---

## Learning Resources

### 📖 Textbooks (Available with Student Pack)
1. **"Numerical Methods for Engineers" by Chapra & Canale**
2. **"Numerical Analysis" by Burden & Faires**
3. **"Introduction to Numerical Analysis" by Stoer & Bulirsch**

### 🌐 Online Resources
1. **Khan Academy**: Calculus and Linear Algebra foundations
2. **MIT OpenCourseWare**: 18.330 (Numerical Methods)
3. **YouTube Channels**:
   - 3Blue1Brown (Linear Algebra visualization)
   - Professor Leonard (Calculus)
   - StatQuest (Statistics & Regression)

### 💻 Practice Platforms
1. **Project Euler**: Mathematical programming challenges
2. **LeetCode**: Algorithm practice
3. **Kaggle**: Real-world data fitting problems

### 🛠️ Tools & Extensions (GitHub Student Pack)
- **GitHub Pro**: Version control your solutions
- **JetBrains**: PyCharm Professional for Python
- **Digital Ocean**: Deploy numerical computing servers
- **Wolfram Alpha**: Verify your solutions

---

## Tips for Success

1. **Start Simple**: Begin with bisection before tackling Newton-Raphson
2. **Visualize**: Always plot the functions and convergence
3. **Compare Methods**: Run different methods on same problem
4. **Test Edge Cases**: What happens with bad initial guesses?
5. **Modify Code**: Change functions, try different parameters
6. **Document**: Keep a notebook of what you learn
7. **Build Projects**: Apply to real data (stock prices, physics simulations)

---

## Common Issues & Solutions

### Import Errors
```bash
ModuleNotFoundError: No module named 'numpy'
```
**Solution**: `pip install numpy pandas matplotlib scipy sympy`

### Convergence Issues
- Check initial guesses (must bracket the root for bisection/regula falsi)
- Increase max iterations
- Decrease tolerance/error
- Try different method

### Matrix Singularity
```
Matrix is singular
```
**Solution**: Matrix has no inverse, check determinant ≠ 0

---

## Next Steps

After mastering these methods:

1. **Implement from Scratch**: Rewrite without NumPy to understand algorithms
2. **Optimize**: Compare performance using `time` module
3. **Real Applications**: 
   - Solve ODEs (Euler, Runge-Kutta)
   - Image processing (interpolation for resizing)
   - Machine Learning (gradient descent is Newton-Raphson!)
4. **Advanced Topics**:
   - Numerical integration (Simpson's rule)
   - Differential equations
   - Finite element methods

---

## Contributing

Found a bug or want to add a method? Feel free to contribute!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

This repository is for educational purposes. Use these implementations to learn, but always cite sources in academic work.

---

## Contact & Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/Ayush080-bct/NumericalMethod/issues)
- **Questions**: Open a [GitHub Discussion](https://github.com/Ayush080-bct/NumericalMethod/discussions) for study help
- **Resources**: Check your GitHub Student Pack benefits at [education.github.com](https://education.github.com/pack)

---

**Happy Learning! 🚀**

*Remember: Numerical methods are everywhere - from weather prediction to Netflix recommendations. Master these fundamentals, and you'll understand how computers solve real-world problems!*

