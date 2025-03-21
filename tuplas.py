# Las tuplas son parecidas a las listas pero sus elementos son inmutables (no se pueden modificar)
# Para crear una tupla de un solo elemento en python, se debe incluir una coma despues del elemento

mi_Tupla = (1 ,2 ,3 ,4 ,5)

print(mi_Tupla)
print(type(mi_Tupla))

print(mi_Tupla[0])
print(mi_Tupla[-1])
print(mi_Tupla[1:3])
print(mi_Tupla[:3])
print(mi_Tupla[3:])

#mi_Tupla[0] = 8 #Marcara error porque las tuplas no se puede modificar.

mi_Tupla2 = (1, "test", [1, 2, 3], 4, True, {'manzanas': 1, 'peras': 5}, 5) # Inmutable
mi_Lista = [1, "test", (1, 2, 3), 4, True, {'manzanas': 1, 'peras': 5}, 5]  # Mutable

print(mi_Tupla2)

for elemento in mi_Tupla2:
    print(elemento)

print("---------------------------------------------")

mi_tupla = (1, 2, 3, 4)

a, b, c, d = mi_tupla
print(a)
print(b)
print(c)
print(d)

print(len(mi_tupla))

mi_primera_tupla = (1, 2, 3, 4 ,5)
mi_segunda_tupla = (6, 7, 8 ,9)
mi_tercera_tupla = mi_primera_tupla + mi_segunda_tupla
print(mi_tercera_tupla)

mi_tupla = (1, 2, 3, 4, 5, 6, 7)

numeros_pares = tuple(i for i in mi_tupla if i % 2 == 0)
print(numeros_pares)