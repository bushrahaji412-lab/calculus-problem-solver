# CALCULUS SOLVER - USAGE GUIDE

## How to Run

```bash
pip install sympy          # install once
python calculus_solver.py  # start the program
```

Select a topic number from the menu, see the example, enter your question.
Navigation commands: **back** (change topic), **quit** (exit).

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

## Topic 16 - Arc Length

Format: `y=<f(x)> from x=<a> to x=<b>`

```
y=x**2 from x=0 to x=1
y=sqrt(x) from x=0 to x=4
```

## Topic 17 - Surface of Revolution

Format: `y=<f(x)> from x=<a> to x=<b>` (around x-axis)

```
y=x**2 from x=0 to x=1
y=sqrt(x) from x=0 to x=4
```

## Topic 18 - Volume of Revolution

Format: `y=<f(x)> from x=<a> to x=<b>` (disk method, around x-axis)

```
y=x from x=0 to x=2
y=x**2 from x=0 to x=1
```

## Topic 19 - Sequences and Limits

Format: `a_n = <expression in n>`

```
a_n = (2*n + 1)/(n + 3)
a_n = n**2/(2*n**2 + 1)
a_n = 1/n
```

## Topic 20 - Infinite Series and Convergence Tests

Format: `sum <expression in n>` (from n=1 to infinity)

```
sum 1/n**2
sum 1/n
sum n/(n**2 + 1)
```

## Topic 21 - Taylor and Maclaurin Series

Format: `<function> about x=<center>` (center=0 gives Maclaurin)

```
sin(x) about x=0
exp(x) about x=0
ln(x) about x=1
cos(x) about x=0
```

## Topic 22 - Power Series

Format: `sum <term in x and n>`

```
sum x**n/factorial(n)
sum x**n/n
sum n*x**n
```

## Topic 23 - Direction Angles, Cosines and Ratios

Format: `vector (<a>, <b>, <c>)`

```
vector (2, 3, 6)
vector (1, -2, 2)
vector (0, 1, 0)
```

## Topic 24 - Parametric Equations of Lines

Format: `point (<x0>,<y0>,<z0>) direction (<a>,<b>,<c>)`

```
point (1, 2, 3) direction (2, -1, 4)
point (0, 0, 0) direction (1, 2, 3)
```

## Topic 25 - Vector Differentiation and Integration

Format: `r(t) = (<x(t)>, <y(t)>, <z(t)>)`
Add `integrate` anywhere to integrate instead of differentiate.

```
r(t) = (t**2, sin(t), exp(t))
r(t) = (3*t, t**2, 2*t**3)
integrate r(t) = (cos(t), t, t**2)
```

## Topic 26 - Equation of Plane

Format 1: `point (<x>,<y>,<z>) normal (<a>,<b>,<c>)`
Format 2: `points (<x1>,<y1>,<z1>), (<x2>,<y2>,<z2>), (<x3>,<y3>,<z3>)`

```
point (1,2,3) normal (1,-1,2)
points (1,0,0), (0,1,0), (0,0,1)
```

## Topic 27 - Equation of Sphere

Format 1: `center (<h>,<k>,<l>) radius <r>`
Format 2: `general <equation>=0`

```
center (1,2,3) radius 5
center (0,0,0) radius 3
general x**2+y**2+z**2-2*x-4*y+4=0
```

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

**Slow response** — Some topics (arc length, surface area, series) involve complex symbolic computation and may take a few seconds.
