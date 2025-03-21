
# Ejercicio 1

"""
def mi_decorador(funcion): # Funcion de orden superior
    def envoltura():
        print("Estoy saludando en la envoltura del decorador antes de llamar a la funcion")
        funcion()
        print("Estoy saludando en la envoltura del decorador despues de llamar a la funcion")
    return envoltura

@mi_decorador
def saludo():

    print("Hola, estoy saludando dentro de la funcion")

saludo()
"""

# Ejercicio 2

"""
class Persona:

    def __init__(self, nombre, edad):

        self._nombre = nombre
        self._edad = edad

    @property
    def edad(self): # Getter
        return self._edad
    
    @edad.setter # Setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError("[!] La edad no puede ser 0 o un numero negativo")
        
manolo = Persona("Manolo", 23)
manolo.edad = 28 #Setter
print(manolo.edad) # Getter
"""

#-----------------------------------------------------------------------------------------------------------------------
# Ejercicio 3
"""
import time

def cronometro(funcion):
    def envoltura():
        inicio = time.time()
        funcion()
        final = time.time()

        print(f"Tiempo total transcurrido en la funcion {funcion.__name__}: {final - inicio}")
    return envoltura


@cronometro
def pausa_corta():
    time.sleep(1)

@cronometro
def pausa_larga():
    time.sleep(2)

pausa_corta()
pausa_larga()
"""
"""
import time

def cronometro(funcion):
    def envoltura(num):
        inicio = time.time()
        funcion(num)
        final = time.time()

        print(f"Tiempo total transcurrido en la funcion {funcion.__name__}: {final - inicio}")
    return envoltura


@cronometro
def pausa_corta(num):
    time.sleep(num)

@cronometro
def pausa_larga(num):
    time.sleep(num)

pausa_corta(2)
pausa_larga(3)
"""
#----------------------------------------------------------------------------------------------------------------------------
"""
# uso de *args

def suma(*args):
    return sum(args)

print(suma(2,3,4))

# uso de **kwargs

def presentacion(**kwargs):

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

presentacion(nombre="Luis", edad=31, ciudad="Navolato", profesion="michologo")
"""
"""
import time

def cronometro(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        funcion()
        final = time.time()

        print(f"Tiempo total transcurrido en la funcion {funcion.__name__}: {final - inicio}")
    return envoltura


@cronometro
def pausa_corta(*args, **kwargs):
    time.sleep(1)

@cronometro
def pausa_larga(*args, **kwargs):
    time.sleep(2)

pausa_corta()
pausa_larga()
"""
"""
import time

def cronometro(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        funcion()
        final = time.time()

        print(f"Tiempo total transcurrido en la funcion {funcion.__name__}: {final - inicio}")

        if args and kwargs:
            print(args)
            print(kwargs)

    return envoltura

@cronometro
def pausa_corta(*args, **kwargs):
    time.sleep(1)

@cronometro
def pausa_larga(*args, **kwargs)
time.sleep(2)

pausa_corta(2,3,4,5,6,7, nombre="Luis", edad=17)
pausa_larga()
"""
class Circunferencia:

    def __init__(self, radio):
        self._radio = radio

    @property #Getter
    def radio(self):
        return self._radio

    @property # Getter
    def diametro(self):
        return 2 * self._radio

    @property
    def area(self):
        return 3.1416 * (self._radio ** 2)

    @radio.setter # Setter
    def radio(self, valor):
        self._radio = valor

c = Circunferencia(5)
print(c.radio)
print(c.diametro)
print(round(c.area, 2))

c.radio = 10
print(c.radio)
print(c.diametro)
print(round(c.area, 2))