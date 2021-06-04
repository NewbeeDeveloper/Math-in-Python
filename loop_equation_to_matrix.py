import sympy as sym
import numpy as np

#Importar símbolos a incógnitas
x = sym.symbols('x')
y = sym.symbols('y')

#Definir longitud de las dimenciones de la matriz
xyset = range(0,3)

#Creación de la función
fxy = (4+x)*(3-y)

#Poblar con ceros a la matriz
outmat = np.zeros([len(xyset),len(xyset)])

#Iterar la matriz para almacenar los resultados de la función
for i in xyset:
    for j in xyset:
        outmat[i,j] = fxy.subs({x:i,y:j})

print(outmat)
