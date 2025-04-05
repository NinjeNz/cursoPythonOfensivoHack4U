def saludo(name):
    print(f"Hola {name}, te mando un saludo!")

saludo("Paco")

def suma(x, y):
    return x + y

resultado = suma(2, 8)
print(f"\n[+] La suma de ambos valores es {resultado}")

def mi_funcion():
    variable_local = "Soy una variable local"
    print(variable_local)

mi_funcion()

# -- Ambitos --
# Variable global: Es una variable visible para todo el codigo.
# Variable local: Es una variable visible solamente en una parte del codigo, por ejemplo, dentro de una funcion.

variable_global = "Soy una variable global"

def mi_funcion2():
    print(variable_global)

mi_funcion2()

print(variable_global)
#----------------------------------
variable = "Soy global"

def mi_funcion2():
    variable = "Soy local"
    print(variable)

mi_funcion2()

print(variable)
#------------------------------------
variable = "Soy global"

def mi_funcion2():
    global variable # Mediante "global" hacemos accesible dentro de una funcion a una variable local
    variable = "Soy global y he sido modificado"
    print(variable)

mi_funcion2()

print(variable)

