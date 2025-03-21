mi_diccionario = {"nombre": "Rolando el Pando", "edad": 28, "isla": "Sorna"}

print(mi_diccionario)
print(type(mi_diccionario))
print(mi_diccionario["nombre"])

mi_diccionario["nombre"] = "Pinolo"
print(mi_diccionario["nombre"])

mi_diccionario["profesion"] = "Programador"
print(mi_diccionario)

if "isla" in mi_diccionario:
    print("Esta clave existe en el diccionario")
else:
    print("Esta clave no existe en el diccionario")

for key, value in mi_diccionario.items():
    print(f"Para la clave {key} tendriamos el valor {value}")

# mi_diccionario.clear() --> Limpia el contenido del diccionario.
print(f"La longitud del diccionario es de {len(mi_diccionario)}")
print(mi_diccionario)

cuadrados = {x: x**2 for x in range(6)}
print(cuadrados)
print(cuadrados.keys())
print(cuadrados.values())
print(mi_diccionario.get("nombr", "No encontrado")) # Devuelve la segunda opcion (No encontrado) cuando la primera no existe en el diccionario.

mi_diccionario2 = {"apellido": "el Pando", "mascota": "gato"}
mi_diccionario.update(mi_diccionario2)
print(mi_diccionario)

my_dict = {
    "nombre": "Rolando",
    "hobbies": {"primero": "apostar", "segundo": "futbol"},
    "edad": 28
}

print(my_dict)
print(len(my_dict))
print(my_dict["hobbies"])
print(my_dict["hobbies"]["primero"])
print(my_dict["hobbies"]["segundo"])

my_dict = {"nombre": "Rolando el Pando", "edad": 28, "isla": "Sorna"}

for element in my_dict:
    print(element)

for element in my_dict.values():
    print(element)

for element in my_dict.keys():
    print(element)

for key, value in my_dict.items():
    print(f"[{key}]: {value}")