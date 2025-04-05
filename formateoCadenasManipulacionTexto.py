nombre = "Laura"
edad = 31
a = 5
b = 7
cadena = "   Hola mundo!!   "
cadena2 = "Hola Mundo!!"
cadena3 = "Hola:Mundo,test"

print("Hola me llamo {} y tengo {} años".format(nombre, edad))
print("Hola me llamo {1} y tengo {0} años".format(edad, nombre))
print(f"Hola me llamo {nombre} y tengo {edad} años")
print(f"La suma de {a} + {b} es {a + b}")

print(cadena.strip()) # .strip() quita espacion y saltos de linea
print(cadena2.lower()) # .lower() convierte todas las letras a minusculas
print(cadena2.upper()) # .upper() convierte todo a mayusculas
print(cadena2.replace('o', 'x')) # reemplaza caracteres

nueva_cadena = cadena.split() # .split() separa los elementos de una cadena colocandolos en una lista
print(nueva_cadena)
nueva_cadena = cadena3.split(':')
print(nueva_cadena)
print(nueva_cadena[0])
print(nueva_cadena[1])

s = "Hola mundo!"
print(s.startswith('H')) # revisa si empieza con lo indicado y devuelve un valor TRUE o FALSE
print(s.endswith('!!'))  # revisa si termina con lo indicado y devuelve un valor TRUE o FALSE
print(s.find("Hola")) # .find() devuelve el indice en el que comienza la cadena indicada, si no la encuentre devuelve -1
print(s.find("mundo"))
print(s.index("Hola")) # .index() devuelve el indice en el que comienza la cadena indicada, si no la encuentre devuelve error
#print(s.index("mundoxx"))

c = "Esta cadena es una prueba para ver el total de caracteres e que contiene esta frase"
print(c.count('e')) # .count() cuenta el numero de veces que aparece el caracter indicado
print(f"\n[+] Total de veces que aparece el caracter 'e' en esta frase: {c.count('e')}")

cadena = ["Hola", "Mundo"]
print(' '.join(cadena)) 

nombres = ["Juan", "Pepito", "Manolito"]
print(f"\n[+] Los nombres son {', '.join(nombres)}") # .join() une cada elemento de una lista con el caracter o cadena indicado.

s = "hola mundo"
print(s.capitalize()) # .capitalize() convierte la primer letra a mayuscula.
print(s.title()) # .title() convierte a mayuscula la primer letra de cada palabra

s = "Hola Mundo"
print(s.swapcase()) # .swapcase() invierte de minuscula a mayuscula y viceversa.

s = "abc"
print(s.isalpha())

s = "abc123"
print(s.isalpha())

s = "123"
print(s.isdigit())

# .isspace()
# .islower()
# .isupper()
# .istitle()

s = "Hola, soy, Manolito, y, no, me, gusta, la, playa"
print(s.replace(',', ''))
print(s.replace(',', '@'))

s = "Hola soy Manolito y no me gusta el desierto"
tabla = str.maketrans('aey', 'zpo')
nueva_cadena = s.translate(tabla)
