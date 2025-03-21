i = 0

while i < 5:
    print(i)
    i+=1

nombres = ["Luis", "Abilene", "Fernando", "Israel", "Dionicio"] #Lista

for nombre in nombres:
    print(f"El nombre para esta vuelta es {nombre}")


for contador, nombre in enumerate(nombres):
    print(f"Nombre [{contador+1}]: {nombre}")

frutas = {"Manzanas": 1, "Platanos": 5, "Kiwis": 3} #Diccionario

for fruta, cantidad in frutas.items():
    print(f"Hay {cantidad} de {fruta}")

# Bucles anidados

my_list = [[1, 4, 5], [2, 6, 8], [9, 4, 1]]

for element in my_list:
    print(element)

for element in my_list:
    for element_in_list in element:
        print(element_in_list)

for element in my_list:
    print(f"\n[+] Vamos a desglosar la lista {element}\n")
    for element_in_list in element:
        print(element_in_list)

#Lista de comprensión

odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]
print(cuadrado)

for i in range(10):

    if i == 5:
        break
    print(i)

for i in range(10):

    print(i)
    if i == 5:
        break
    
for i in range(10):
    
    if i == 5:
        continue # Cuando se cumple la condicion 'Continue" hace que se salte a la siguiente iteracion sin realizar la accion.
    print(i)

for i in range(10):

    if i == 5:
        print("Actualmente 'i' vale 5")
    else:
        print(f"Actualmente 'i' NO vale 5 pues vale: [{i}]")

for i in range(10):
    
    if i == 10:
        break

else:
    print("Bucle concluido exitosamente")

# -------------------------------------------
print("Continuamos con la ejecucion del resto de instrucciones")

i = 0

while i < 16:
    if i == 10:
        print("Salimos antes de tiempo")
        break
    i += 1
else:
    print("El bucle while ha finalizado exitosamente")
#----------------------------------------------
print("Estamos fuera del bucle")

edad = 18

if edad < 13:
    print("Eres un crio")
elif 13 <= edad < 18:
    print("Eres un adolecente")
else:
    print("Eres una adulto")

edad = 20
nacionalidad = "mexicana"
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

edad = 20
nacionalidad = "japones"

if edad >= 18 and nacionalidad == "mexicana":
    print("Puedes votar en las elecciones mexicanas")
else:
    print("No eres mexicano bro")

mi_lista = [1, 4, 6, 12, 14, 18, 79]

if 1 in mi_lista:
    print("Este numero esta en la lista")
else:
    print("Este numnero No esta en la lista")

edad = 20
nacionalidad = "argentino"

# Condicional anidado
if edad >= 18:
    if nacionalidad == "argentino":
        print("Puedes votar en las elecciones argentinas")

numbers = [2, 4, 6, 8, 10, 12, 9, 14]
todos_son_pares = True

for number in numbers:
    if number % 2 != 0:
        todos_son_pares = False
        break

if todos_son_pares:
    print("Todos los elementos de la lista son pares")
else:
    print("Alguno de los elementos de la lista es impar")