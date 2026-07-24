# COMPREHENSIVE CALCULUS PROBLEM SOLVER

A Python application that solves calculus problems across **18 topics** using a numbered topic-selection menu.

---

## Quick Start

### 1. Install requirement
```bash
pip install sympy
```

### 2. Run the interactive solver
```bash
python calculus_solver.py
```

---

## How It Works

```
Start
  |
  v
Display topic menu (1-18)
  |
  v
You select a topic number (e.g., 4 for Differentiation)
  |
  v
Program shows an example for that topic
  |
  v
You enter your question
  |
  v
SymPy computes and displays the solution
  |
  v
Return to the main menu after completing a calculation.
Select another topic or enter 0 to exit the program.
---

## 18 Topics

| # | Topic |
|---|-------|
| 1 | Limits and Continuity |
| 2 | L'Hopital's Rule |
| 3 | Continuity |
| 4 | Basic Differentiation |
| 5 | Leibniz Theorem (Product / Quotient Rule) |
| 6 | Rolle's Theorem |
| 7 | Mean Value Theorem (MVT) |
| 8 | Extrema of One Variable Function |
| 9 | Applied Maximum and Minimum Problems |
| 10 | Extrema of Two Variables Function |
| 11 | Constrained Optimization (Lagrange Multipliers) |
| 12 | Integration by Parts |
| 13 | Improper Integrals |
| 14 | Integration by Partial Fractions |
| 15 | Area Under Curve / Between Curves |
| 16 | volume problems |
| 17 | Taylor series |
| 18 | Maclaurin series |

---

## Example Session

```
Select topic: 4
Topic: Basic Differentiation
Example: x**3 + 2*x**2 + 5*x

>> x**3 + 2*x**2 + 5*x

SOLUTION:
f(x)   = x**3 + 2*x**2 + 5*x
f'(x)  = 3*x**2 + 4*x + 5
f''(x) = 6*x + 4
```

---

## Notation Guide

| You type | Meaning |
|----------|---------|
| `x**2`   | x squared |
| `exp(x)` | e^x |
| `ln(x)`  | natural log |
| `sqrt(x)`| square root |
| `sin(x)`, `cos(x)`, `tan(x)` | trig |
| `pi`     | pi |
| `oo`     | infinity |
| `**`     | exponentiation (also `^` works) |

---

## Files

| File | Purpose |
|------|---------|
| `calculus_solver.py` | Main program — run this
| `USAGE_GUIDE.md` | Examples for every topic |
| `README.md` | This file |
