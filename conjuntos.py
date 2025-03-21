# Conjuntos (Sets)

mi_conjunto = {1, 2, 3}
print(type(mi_conjunto))
print(mi_conjunto)

mi_conjunto.add(4)
print(mi_conjunto)

mi_conjunto.update({4, 5, 6})
print(mi_conjunto)

mi_conjunto.remove(3)
print(mi_conjunto)

mi_conjunto.discard(7) # Elimina el elemento en caso de existir, y en caso de no existir simplemente no hace nada.

mi_primer_conjunto = {1, 2, 3, 4, 5}
mi_segundo_conjunto = {3, 4, 5, 6, 7}

conjunto_final = mi_primer_conjunto.intersection(mi_segundo_conjunto) # Muestra los elementos que se repiten.
print(conjunto_final)

conjunto_final = mi_primer_conjunto.union(mi_segundo_conjunto) # Une los elementos sin mostrar los repeqitidos.
print(conjunto_final)

# Subconjunto
primer_conjunto = {1, 2, 3}
segundo_conjunto = {1, 2, 3, 4, 5, 6, 7}

print(primer_conjunto.issubset(segundo_conjunto)) # issubset evalua si el conjunto es subconjunto del otro y regresa un valor boolean.

primer_conjunto = {"Hackermate", "s4vitar", "MariaDB"}
segundo_conjunto = {"Pepito", "Manolo", "s4vitar", "Lobotec", "Hackermate"}
print(primer_conjunto.issubset(segundo_conjunto))

mi_lista = [1, 5, 4, 6, 5, 1, 2, 2, 2, 8, 12, 14, 12, 1, 1]
no_repeat = set(mi_lista)
print(no_repeat)
no_repeat = list(set(mi_lista))
print(no_repeat)

mi_conjunto = set(range(10000))
print(1234 in mi_conjunto) # True
print(123477 in mi_conjunto) # False

# Quiero saber que usuarios estan en ambas plataformas
usuarios_facebook = {"Ana", "S4vitar", "Hackermate", "Lobotec"}
usuarios_X = {"Hackermate", "S4vitar", "Manolo", "Pinolo"}
ambas_plataformas = usuarios_facebook.intersection(usuarios_X)
print(ambas_plataformas)
# Todos los usuarios de ambas plataformas
todos_los_usuarios = usuarios_facebook.union(usuarios_X)
print(todos_los_usuarios)