import sympy as sym

x = sym.symbols('x')

expr = 2 * x + 4 - 9

print("Solution %s is x =  %g" % (sym.latex(expr), sym.solve(expr)[0]))
