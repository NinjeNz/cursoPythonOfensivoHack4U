class Persona:

    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
         return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
marcelo = Persona("Marcelo", 28)
luis = Persona("Luis", 31)
print(marcelo.saludo())
print(luis.saludo())

class Animal:

    def __init__(self, nombre, animal): #Animal.__init__(gato, nombre, animal)

        self.nombre = nombre
        self.animal = animal

    def descripcion(self): # Animal.descripcion(obj)

        print(f"{self.nombre} es un {self.animal}")

gato = Animal("Ryu", "Gato")
perro = Animal("Roger", "Perro")
        
gato.descripcion()
perro.descripcion()

class CuentaBancaria:

    def __init__(self, cuenta, nombre, dinero=0):

        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, dinero): # CuentaBancaria.depositar_dinero(manolo)
        self.dinero += dinero

        return f"\n[+] [{self.nombre}] Se han depositado {dinero} dolares, actualmente el balance de la cuenta es de {self.dinero} dolares"

    def retirar_dinero(self, dinero):

        if dinero > self.dinero:
            return f"\n[!] [{self.nombre}] Operacion denegada: Fondos Insuficientes\n"

        self.dinero -= dinero # self.dinero = self.dinero -dinero

        return f"\n[+] [{self.nombre}] Se han retirado {dinero} dolares, actualmente el balance de la cuenta es de {self.dinero} dolares"

manolo = CuentaBancaria("234235", "Manolo Polo", 1000)
pinolo = CuentaBancaria("875895", "Pinolo Lolo", 10)

print(manolo.depositar_dinero(500))
print(manolo.retirar_dinero(900))
print(manolo.retirar_dinero(1800))

print(pinolo.retirar_dinero(5))

class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property # Decorador que se utiliza para definir metodos en una clase que se comportan como atributos.
    def area(self): # Rectangulo.area(rect1)
        return self.ancho * self.alto

    def __str__(self): # permite ejecutar algo printeando directamente el objeto
        return f"\n[+] Propiedades del rectangulo: [Ancho {self.ancho}][Alto: {self.alto}]"

    def __eq__(self, self2): # Igualdad
        return self.ancho == self2.ancho and self.alto == self2.alto

rect1 = Rectangulo(20, 80)
rect2 = Rectangulo(20, 80)

print(rect1) # con __str__       
#print(f"\n[+] El area es {rect1.area()}") # Sin @property
print(f"\n[+] El area es {rect1.area}") # Se puede ejecutar debido a @property
print(f"\n ¿Son iguales? -> {rect1 == rect2}")

        
