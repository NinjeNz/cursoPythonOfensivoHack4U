mi_funcion = lambda: "Hola mundo!"
print(mi_funcion())

cuadrado = lambda x: x**2
print(cuadrado(7))

suma = lambda x, y: x+y
print(suma(7, 8))

# funciones lambda anonimas con map()
# map() --> Realiza la operacion que le indiques por cada elemento dentro de un objeto iterable,
#           recibe dos parametros, el primero es la operatoria a realizar y el segundo el objeto iterable.
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# funciones lambda anonimas con filter()
# map() --> Realiza la operacion que le indiques mas un condicionante por cada elemento dentro de un objeto
#           iterable regresando unicamente como resultado los valores que fueron TRUE.
#           Recibe dos parametros, el primero es la operatoria a realizar y el segundo el objeto iterable.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# reduce() recicla todos los resultados para usarlos como input en cada iteracion hasta llegar al resultado final.
from functools import reduce
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x*y, numeros)
print(producto)
