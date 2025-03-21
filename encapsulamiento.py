# Ejemplo 1
"""
class Ejemplo:

    def __init__(self):

        # Atributo protegido
        #self._atributo_protegido = "soy un atributo protegido y no deberias poder verme"

        # Atributo privado
         self.__atributo_privado = "Soy un atributo privado y no deberias poder verme" # Por debajo python hace uso de "name mangling"

ejemplo = Ejemplo()
#print(ejemplo._atributo_protegido)
print(ejemplo.__atributo_privado) # por debajo python coloca el siguiente nombre al atributo haciendo uso de name mangling: print(ejemplo._Ejemplo__atributo_privado)
"""
"""
# Ejemplo 2

class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0 # Atributo privado

    def conducir(self, kilometros):
        if kilometros >= 0:
            self.__kilometraje += kilometros
        else:
            print("\n[!] Los kilometros deben ser mayores a 0\n")

    def mostrar_kilometros(self):
        return self.__kilometraje

coche = Coche("Toyota", "Supra")
coche.conducir(150)
print(coche.mostrar_kilometros())
"""

# Ejemplo 3

class CuentaBancaria:

    def __init__(self, num_cuenta, titular, saldo_inicial=0):

        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial # Atributo privado

    def depositar_dinero(self, cantidad):

        if cantidad > 0:
            self.__saldo += cantidad
            print(f"\n[+] Saldo actual en la cuenta: {self.__saldo}")
        else:
            print(f"[!] El monto a depositar es incorrecto")

    def retirar_dinero(self, cantidad):

        if cantidad > 0:
            if cantidad > self.__saldo:
                print(f"\n[!] La cantidad a retirar supera el dinero actual de la cuenta")
            else:
                self.__saldo -= cantidad
                print(f"\n[+] Saldo actual en la cuenta: {self.__saldo}")

        else:
            print(f"\n[!] El monto a retirar es incorrecto")

    def mostrar_dinero(self):

        return f"\n[+] El saldo actual en la cuenta es: {self.__saldo}\n"

manolo = CuentaBancaria("87575856", "Manolo Pinolo", 1500)
manolo.depositar_dinero(500)
manolo.retirar_dinero(200)

print(manolo.mostrar_dinero())

