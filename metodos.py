# Proyecto calculadora

# Usando  @staticmethod
class Calculadora:

    @staticmethod
    def suma(num1, num2):
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2):
        return num1 - num2
    
    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2
    
    @staticmethod
    def division(num1, num2):
        return num1 / num2 if num2 != 0 else "[!] Error: No se puede dividir un numero entre 0"

print(Calculadora.suma(2, 8))
print(Calculadora.resta(2, 8))
print(Calculadora.multiplicacion(2, 8))
print(Calculadora.division(2, 8))
print(Calculadora.division(2, 0)) # Marcara error porque no se puede dividir un numero entre 0
print("\n")


# Usando @classmethod
class Automovil:

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "Deportivo")
    
    @classmethod
    def sedan(cls, marca):
        return cls(marca, "Sedan")
    
    def __str__(self):
        return f"La marca {self.marca} es un modelo {self.modelo}"
    
#deportivo = print(Automovil.deportivos("Ferrari"))
deportivo = Automovil.deportivos("Ferrari")
print(deportivo)
#sedan = print(Automovil.sedan("Toyota"))
sedan = Automovil.sedan("Toyota")
print(sedan)

print("\n")

#------------------------------------------------------------

class Estudiantes:

    estudiantes = [] # Esta es una variable de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18 # Unicamente devuelve un valor ya sea True o False

    @classmethod
    def crear_estudiantes(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad) # Retora un objeto de la propia clase (cls) con el nombre y edad
        else:
            print(f"\n[!] Error: El estudiante {nombre} es menor de edad")

    @staticmethod
    def mostrar_edtudiantes():
        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(f"\t[+] Estudiante numero [{i+1}]: {estudiante.nombre}")


Estudiantes.crear_estudiantes("Hackermate", 43)
Estudiantes.crear_estudiantes("S4vitar", 28)
Estudiantes.crear_estudiantes("Xerosec", 12)
Estudiantes.crear_estudiantes("Hackavis", 8)

print("\n[i] Listando los estudiantes existentes:\n")
Estudiantes.mostrar_edtudiantes()