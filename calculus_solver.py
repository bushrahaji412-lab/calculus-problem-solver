#!/usr/bin/env python3

"""
CALCULUS PROBLEM SOLVER1

Topics Included:
1. Limits
2. Continuity
3. L'Hospital Rule
4. Differentiation
5. Leibniz Rule
6. Rolle's Theorem
7. Mean Value Theorem
8. One Variable Extrema
9. Applied Optimization
10. Two Variable Extrema
11. Lagrange Multipliers
12. Integration by Parts
13. Improper Integrals
14. Partial Fractions
15. Area Problems
16. Volume Problems
17. Taylor Series
18. Maclaurin Series
"""

import sympy as sp
from sympy import *
import re


class CalculusSolver:

    def __init__(self):

        self.x, self.y = symbols('x y')

        self.topics = {
            1: "Limits",
            2: "Continuity",
            3: "L'Hospital Rule",
            4: "Differentiation",
            5: "Leibniz Rule",
            6: "Rolle's Theorem",
            7: "Mean Value Theorem",
            8: "One Variable Extrema",
            9: "Applied Optimization",
            10: "Two Variable Extrema",
            11: "Lagrange Multipliers",
            12: "Integration by Parts",
            13: "Improper Integrals",
            14: "Partial Fractions",
            15: "Area Problems",
            16: "Volume Problems",
            17: "Taylor Series",
            18: "Maclaurin Series"
        }

    # =========================================================
    # PARSER
    # =========================================================

    def parse(self, expr):

        expr = expr.replace("^", "**")

        local_dict = {
            'x': self.x,
            'y': self.y,
            'sin': sin,
            'cos': cos,
            'tan': tan,
            'exp': exp,
            'log': log,
            'ln': log,
            'sqrt': sqrt,
            'pi': pi,
            'oo': oo,
            'e': E
        }

        return sympify(expr, locals=local_dict)

    # =========================================================
    # 1. LIMITS
    # =========================================================

    def solve_limits(self):

        print("\nExample: lim x->0, sin(x)/x")

        q = input("Enter limit: ")

        m = re.search(r'lim x->(.+?),(.+)', q)

        if not m:
            print("Invalid format")
            return

        point = self.parse(m.group(1).strip())
        expr = self.parse(m.group(2).strip())

        result = limit(expr, self.x, point)

        print("\nFunction =", expr)
        print("Point =", point)
        print("Answer =", result)

    # =========================================================
    # 2. CONTINUITY
    # =========================================================

    def solve_continuity(self):

        print("\nExample:")
        print("Function: (x**2 - 4)/(x - 2)")
        print("Point: 2")

        expr = input("\nEnter function: ")
        point = input("Enter point: ")

        f = self.parse(expr)
        a = self.parse(point)

        left = limit(f, self.x, a, '-')
        right = limit(f, self.x, a, '+')

        try:
            value = f.subs(self.x, a)
        except:
            value = "Undefined"

        print("\nLeft Limit =", left)
        print("Right Limit =", right)
        print("f(a) =", value)

        if left == right == value:
            print("Function is CONTINUOUS")
        else:
            print("Function is NOT continuous")

    # =========================================================
    # 3. L'HOSPITAL RULE
    # =========================================================

    def solve_lhospital(self):

        print("\nExample: lim x->0, sin(x)/x")

        q = input("Enter limit: ")

        m = re.search(r'lim x->(.+?),(.+)', q)

        if not m:
            print("Invalid format")
            return

        point = self.parse(m.group(1).strip())
        expr = self.parse(m.group(2).strip())

        num, den = fraction(expr)

        dnum = diff(num, self.x)
        dden = diff(den, self.x)

        result = limit(dnum / dden, self.x, point)

        print("\nNumerator Derivative =", dnum)
        print("Denominator Derivative =", dden)
        print("Answer =", result)

    # =========================================================
    # 4. DIFFERENTIATION
    # =========================================================

    def solve_derivative(self):

        print("\nExample: x**3 + 2*x**2 + 5*x")

        expr = input("Enter function: ")

        f = self.parse(expr)

        d1 = diff(f, self.x)
        d2 = diff(d1, self.x)

        print("\nf(x) =", f)
        print("f'(x) =", d1)
        print("f''(x) =", d2)

    # =========================================================
    # 5. LEIBNIZ RULE
    # =========================================================

    def solve_leibniz(self):

        print("\nExample:")
        print("u = x**2")
        print("v = sin(x)")

        u_expr = input("\nEnter u(x): ")
        v_expr = input("Enter v(x): ")

        u = self.parse(u_expr)
        v = self.parse(v_expr)

        du = diff(u, self.x)
        dv = diff(v, self.x)

        result = du * v + u * dv

        print("\nu'(x) =", du)
        print("v'(x) =", dv)
        print("d/dx(u*v) =", simplify(result))

    # =========================================================
    # 6. ROLLE'S THEOREM
    # =========================================================

    def solve_rolles(self):

        print("\nExample:")
        print("Function: x**2 - 4*x + 3")
        print("a = 1")
        print("b = 3")

        expr = input("\nEnter function: ")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))

        f = self.parse(expr)

        fa = f.subs(self.x, a)
        fb = f.subs(self.x, b)

        print("\nf(a) =", fa)
        print("f(b) =", fb)

        if fa != fb:
            print("Rolle's theorem does not apply")
            return

        fp = diff(f, self.x)

        print("\nf'(x) =", fp)

        c_values = solve(fp, self.x)

        for c in c_values:
            if a < float(c) < b:
                print("c =", c)

    # =========================================================
    # 7. MVT
    # =========================================================

    def solve_mvt(self):

        print("\nExample:")
        print("Function: x**3")
        print("a = 0")
        print("b = 2")

        expr = input("\nEnter function: ")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))

        f = self.parse(expr)

        slope = (f.subs(self.x, b) - f.subs(self.x, a)) / (b - a)

        fp = diff(f, self.x)

        c_values = solve(fp - slope, self.x)

        print("\nAverage Slope =", slope)
        print("f'(x) =", fp)

        for c in c_values:
            if a < float(c) < b:
                print("c =", c)

    # =========================================================
    # 8. ONE VARIABLE EXTREMA
    # =========================================================

    def solve_extrema(self):

        print("\nExample: x**3 - 3*x**2 + 2")

        expr = input("Enter function: ")

        f = self.parse(expr)

        fp = diff(f, self.x)
        fpp = diff(fp, self.x)

        critical_points = solve(fp, self.x)

        print("\nf'(x) =", fp)
        print("f''(x) =", fpp)

        for c in critical_points:

            second = fpp.subs(self.x, c)

            print("\nCritical Point =", c)

            if second > 0:
                print("Local Minimum")
            elif second < 0:
                print("Local Maximum")
            else:
                print("Inconclusive")

    # =========================================================
    # 9. APPLIED OPTIMIZATION
    # =========================================================

    def solve_optimization(self):

        print("\nExample: maximize x*y subject to x+y=10")

        q = input("Enter question: ")

        m = re.search(r'(maximize|minimize) (.+?) subject to (.+)', q)

        if not m:
            print("Invalid format")
            return

        goal = m.group(1)

        f = self.parse(m.group(2))

        constraint = m.group(3)

        lhs, rhs = constraint.split("=")

        g = self.parse(lhs) - self.parse(rhs)

        y_expr = solve(g, self.y)[0]

        new_f = f.subs(self.y, y_expr)

        derivative = diff(new_f, self.x)

        critical = solve(derivative, self.x)

        print("\nReduced Function =", new_f)

        for c in critical:

            y_val = y_expr.subs(self.x, c)

            value = f.subs([(self.x, c), (self.y, y_val)])

            print("\nPoint =", (c, y_val))
            print("Value =", value)

    # =========================================================
    # 10. TWO VARIABLE EXTREMA
    # =========================================================

    def solve_two_variable_extrema(self):

        print("\nExample: x**2 + y**2 - 2*x - 4*y")

        expr = input("Enter function: ")

        f = self.parse(expr)

        fx = diff(f, self.x)
        fy = diff(f, self.y)

        critical = solve([fx, fy], [self.x, self.y])

        print("\nfx =", fx)
        print("fy =", fy)

        print("\nCritical Points =", critical)

    # =========================================================
    # 11. LAGRANGE MULTIPLIERS
    # =========================================================

    def solve_lagrange(self):

        print("\nExample: maximize x*y subject to x+y=10")

        q = input("Enter question: ")

        m = re.search(r'(maximize|minimize) (.+?) subject to (.+)', q)

        if not m:
            print("Invalid format")
            return

        f = self.parse(m.group(2))

        constraint = m.group(3)

        lhs, rhs = constraint.split("=")

        g = self.parse(lhs) - self.parse(rhs)

        lam = symbols('lambda')

        eq1 = diff(f, self.x) - lam * diff(g, self.x)
        eq2 = diff(f, self.y) - lam * diff(g, self.y)

        solutions = solve([eq1, eq2, g], [self.x, self.y, lam])

        print("\nSolutions:")
        print(solutions)

    # =========================================================
    # 12. INTEGRATION BY PARTS
    # =========================================================

    def solve_integration_parts(self):

        print("\nExample: x*exp(x)")

        expr = input("Enter expression: ")

        f = self.parse(expr)

        result = integrate(f, self.x)

        print("\nIntegral =", result, "+ C")

    # =========================================================
    # 13. IMPROPER INTEGRALS
    # =========================================================

    def solve_improper_integrals(self):

        print("\nExample: 1/x**2 from 1 to oo")

        q = input("Enter question: ")

        m = re.search(r'(.+?) from (.+?) to (.+)', q)

        if not m:
            print("Invalid format")
            return

        expr = self.parse(m.group(1))
        a = self.parse(m.group(2))
        b = self.parse(m.group(3))

        result = integrate(expr, (self.x, a, b))

        print("\nAnswer =", result)

    # =========================================================
    # 14. PARTIAL FRACTIONS
    # =========================================================

    def solve_partial_fraction(self):

        print("\nExample: 1/(x**2 - 1)")

        expr = input("Enter rational expression: ")

        f = self.parse(expr)

        result = apart(f)

        print("\nPartial Fraction:")
        print(result)

    # =========================================================
    # 15. AREA PROBLEMS
    # =========================================================

    def solve_area(self):

        print("\n1. Area Under Curve")
        print("2. Area Between Two Curves")

        choice = input("\nEnter choice: ")

        if choice == '1':

            print("\nExample: x**2 from 0 to 2")

            q = input("Enter question: ")

            m = re.search(r'(.+?) from (.+?) to (.+)', q)

            if not m:
                print("Invalid format")
                return

            expr = self.parse(m.group(1))
            a = self.parse(m.group(2))
            b = self.parse(m.group(3))

            area = integrate(expr, (self.x, a, b))

            print("\nArea =", area)

        elif choice == '2':

            print("\nExample: x, x**2 from 0 to 1")

            q = input("Enter question: ")

            m = re.search(r'(.+?),(.+?) from (.+?) to (.+)', q)

            if not m:
                print("Invalid format")
                return

            upper = self.parse(m.group(1))
            lower = self.parse(m.group(2))
            a = self.parse(m.group(3))
            b = self.parse(m.group(4))

            area = integrate(upper - lower, (self.x, a, b))

            print("\nArea =", simplify(area))

    # =========================================================
    # 16. VOLUME PROBLEMS
    # =========================================================

    def solve_volume(self):

        print("\n1. Disc and Washer Method")
        print("2. Cylindrical Shell Method")

        choice = input("\nEnter choice: ")

        if choice == '1':

            print("\nExample: x**2 from 0 to 2")

            q = input("Enter question: ")

            m = re.search(r'(.+?) from (.+?) to (.+)', q)

            if not m:
                print("Invalid format")
                return

            expr = self.parse(m.group(1))
            a = self.parse(m.group(2))
            b = self.parse(m.group(3))

            volume = pi * integrate(expr**2, (self.x, a, b))

            print("\nVolume =", simplify(volume))

        elif choice == '2':

            print("\nExample: x**2 from 0 to 2")

            q = input("Enter question: ")

            m = re.search(r'(.+?) from (.+?) to (.+)', q)

            if not m:
                print("Invalid format")
                return

            expr = self.parse(m.group(1))
            a = self.parse(m.group(2))
            b = self.parse(m.group(3))

            volume = 2 * pi * integrate(self.x * expr, (self.x, a, b))

            print("\nVolume =", simplify(volume))

    # =========================================================
    # 17. TAYLOR SERIES
    # =========================================================

    def solve_taylor(self):

        print("\nExample: sin(x), point=0, terms=5")

        q = input("Enter question: ")

        m = re.search(r'(.+?), point=(.+?), terms=(.+)', q)

        if not m:
            print("Invalid format")
            return

        expr = self.parse(m.group(1))
        point = self.parse(m.group(2))
        terms = int(m.group(3))

        result = series(expr, self.x, point, terms)

        print("\nTaylor Series:")
        print(result)

    # =========================================================
    # 18. MACLAURIN SERIES
    # =========================================================

    def solve_maclaurin(self):

        print("\nExample: exp(x), terms=6")

        q = input("Enter question: ")

        m = re.search(r'(.+?), terms=(.+)', q)

        if not m:
            print("Invalid format")
            return

        expr = self.parse(m.group(1))
        terms = int(m.group(2))

        result = series(expr, self.x, 0, terms)

        print("\nMaclaurin Series:")
        print(result)

    # =========================================================
    # MAIN PROGRAM
    # =========================================================

    def run(self):

        while True:

            print("\n" + "=" * 60)
            print("CALCULUS PROBLEM SOLVER")
            print("=" * 60)

            for key, value in self.topics.items():
                print(f"{key}. {value}")

            print("0. Exit")

            choice = input("\nEnter topic number: ")

            if choice == '0':
                print("Goodbye!")
                break

            elif choice == '1':
                self.solve_limits()

            elif choice == '2':
                self.solve_continuity()

            elif choice == '3':
                self.solve_lhospital()

            elif choice == '4':
                self.solve_derivative()

            elif choice == '5':
                self.solve_leibniz()

            elif choice == '6':
                self.solve_rolles()

            elif choice == '7':
                self.solve_mvt()

            elif choice == '8':
                self.solve_extrema()

            elif choice == '9':
                self.solve_optimization()

            elif choice == '10':
                self.solve_two_variable_extrema()

            elif choice == '11':
                self.solve_lagrange()

            elif choice == '12':
                self.solve_integration_parts()

            elif choice == '13':
                self.solve_improper_integrals()

            elif choice == '14':
                self.solve_partial_fraction()

            elif choice == '15':
                self.solve_area()

            elif choice == '16':
                self.solve_volume()

            elif choice == '17':
                self.solve_taylor()

            elif choice == '18':
                self.solve_maclaurin()

            else:
                print("Invalid choice")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    solver = CalculusSolver()
    solver.run()