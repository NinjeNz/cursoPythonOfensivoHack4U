# Ejemplo haciendo uso de Herencia

"""class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este metodo")

class Gato(Animal):

    def hablar(self):
        return f"{self.nombre} dice ¡Miaua!"
        
class Perro(Animal):

    def hablar(self):
        return f"{self.nombre} dice ¡Guau!"

        
gato = Gato("Ryu")
perro = Perro("Rogger")


print(gato.hablar())
print(perro.hablar())

"""

# Ejemplo con polimorfismo

"""class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este metodo")

class Gato(Animal):

    def hablar(self):
        return f"¡Miau!"
        
class Perro(Animal):

    def hablar(self):
        return f"¡Guau!"

def hacer_hablar(object): # Metodo polimorfico

    print(f"{object.nombre} dice {object.hablar()}")
        
gato = Gato("Ryu")
perro = Perro("Rogger")

hacer_hablar(gato)
hacer_hablar(perro)"""

"""class Dispositivo:

    def __init__(self, modelo):
        self.modelo = modelo
    def escanear_vulnerabilidades(self):
        raise NotImplementedError("Este metodo debe ser definido para el resto de subclases existentes")

class Ordenador(Dispositivo):

    def escanear_vulnerabilidades(self):
        return f"[+] Analisis de vulnerabilidades concluido: Actualizacion de software necesaria, multiples desactualizaciones de software detectadas"

class Router(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[+] Analisis de vulnerabilidades concluido: Multiples puertos criticos detectados como abiertos, es recomendable cerrar estos puertos"


class TelefonoMovil(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[+] Analisis de vulnerabilidades concluido: Multiples aplicaciones detectadas con permisos excesivos"

def realizar_escaneo(dispositivo):
    print(dispositivo.escanear_vulnerabilidades())

pc = Ordenador("Lenovo Legion")
router = Router("TP-Link 200")
movil = TelefonoMovil("Samsung Galaxy S24 Ultra")

realizar_escaneo(pc)
realizar_escaneo(router)
realizar_escaneo(movil)"""

# Herencia y polimorfismo y uso de super()

class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def saludo(self):

        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

class Empleado(Persona):

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def saludo(self):

        return f"{super().saludo()}, y cobro {self.salario} dolares brutos anuales"

persona = Empleado("Alicia", 23, 35000)
print(persona.saludo())