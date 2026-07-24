# CALCULUS SOLVER - USAGE GUIDE

## How to Run

```bash
pip install sympy          # install once
python calculus_solver.py  # start the program
```

Select a topic number from the menu, see the example, enter your question.
To exit the program, select option 0 from the main menu.

---

## Topic 1 - Limits and Continuity

Format: `lim x-><point>, <expression>`

```
lim x->2, x**2 + 3*x
lim x->0, sin(x)/x
lim x->oo, (3*x**2 + 2)/(x**2 + 1)
```

## Topic 2 - L'Hopital's Rule

Format: `lim x-><point>, <numerator>/<denominator>`

```
lim x->0, sin(x)/x
lim x->0, (1 - cos(x))/x**2
lim x->oo, x/exp(x)
```

## Topic 3 - Continuity

Format: `f(x) = <expression> at x=<point>`

```
f(x) = x**2 + 3*x at x=2
f(x) = (x**2 - 4)/(x - 2) at x=2
f(x) = 1/x at x=0
```

## Topic 4 - Basic Differentiation

Format: `<expression in x>` (just type the function)

```
x**3 + 2*x**2 + 5*x
sin(x) + cos(x)
exp(x) * x**2
ln(x) / x
```

## Topic 5 - Leibniz (Product / Quotient Rule)

Format: `product: <u>, <v>` or `quotient: <u>, <v>`

```
product: x**2, sin(x)
product: exp(x), ln(x)
quotient: x**2, cos(x)
quotient: sin(x), x
```

## Topic 6 - Rolle's Theorem

Format: `f(x) = <expression>, a=<val>, b=<val>`

```
f(x) = x**2 - 4*x + 3, a=1, b=3
f(x) = x**3 - x, a=-1, b=1
```

## Topic 7 - Mean Value Theorem (MVT)

Format: `f(x) = <expression>, a=<val>, b=<val>`

```
f(x) = x**3, a=0, b=2
f(x) = x**2 + x, a=1, b=4
```

## Topic 8 - Extrema of One Variable

Format: `<expression in x>` (just type the function)

```
x**3 - 3*x**2 + 2
x**4 - 2*x**2
x**2 * exp(-x)
```

## Topic 9 - Applied Optimization

Format: `maximize/minimize <expr> subject to <constraint>`

```
maximize x*y subject to x + y = 10
minimize x**2 + y**2 subject to x + y = 4
```

## Topic 10 - Extrema of Two Variables

Format: `<expression in x and y>`

```
x**2 + y**2 - 2*x - 4*y
x**2 - x*y + y**2 - 2*x
x**3 + y**3 - 3*x - 3*y
```

## Topic 11 - Lagrange Multipliers

Format: `maximize/minimize <f(x,y)> subject to <g(x,y)=c>`

```
maximize x*y subject to x + y = 10
minimize x**2 + y**2 subject to x + 2*y = 4
```

## Topic 12 - Integration by Parts

Format: `<integrand expression>` (type the full integrand)

```
x * exp(x)
x**2 * sin(x)
x * ln(x)
```

## Topic 13 - Improper Integrals

Format: `<expression> from <a> to <b>` (use `oo` for infinity)

```
1/x**2 from 1 to oo
exp(-x) from 0 to oo
1/sqrt(x) from 0 to 1
```

## Topic 14 - Integration by Partial Fractions

Format: `<rational expression>`

```
1/(x**2 - 1)
(3*x + 5)/(x**2 + 5*x + 6)
x/(x**2 - 5*x + 6)
```

## Topic 15 - Area Under / Between Curves

Format:
- Between two curves: `y=<f1> and y=<f2> from x=<a> to x=<b>`
- Area under one curve: `y=<f> from x=<a> to x=<b>`

```
y=x**2 and y=x from x=0 to x=1
y=sin(x) from x=0 to x=pi
y=x**2 and y=2*x from x=0 to x=2
```

 ## Topic 16 - Volume Problems
Options:
1. Disc and Washer Method
2. Cylindrical Shell Method

Format: <expression> from <a> to <b>

Examples:

x**2 from 0 to 2
x from 0 to 2
```

## Topic 17 - Taylor Series

Format: <expression>, point=<point>, terms=<number>

Examples:

sin(x), point=0, terms=5
exp(x), point=1, terms=6

## Topic 18 - Maclaurin Series

Format: <expression>, terms=<number>

Examples:

exp(x), terms=6
sin(x), terms=7

---

## Notation Reference

| Symbol | How to type it |
|--------|---------------|
| x^2    | `x**2` or `x^2` |
| e^x    | `exp(x)` |
| ln(x)  | `ln(x)` |
| sqrt   | `sqrt(x)` |
| pi     | `pi` |
| inf    | `oo` |
| sin/cos/tan | `sin(x)`, `cos(x)`, `tan(x)` |
| arcsin | `asin(x)` |
| sinh   | `sinh(x)` |

---

## Troubleshooting

**"Could not parse"** — Check the format shown in the example prompt. Use `**` for powers, `exp(x)` for e^x.

**Wrong answer** — Double-check your expression uses `*` for multiplication (e.g., `2*x` not `2x`).

**Slow response** — Some symbolic computations such as optimization, integration, and Taylor series may take a few seconds.