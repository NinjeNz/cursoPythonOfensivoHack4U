#!/usr/bin/env python3

class Vehiculo:

    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"\n[!] El vehiculo con matricula {self.matricula} no se puede alquilar")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"\n[!] El vehiculo con matricula {self.matricula} no se puede devolver porque no ha sido alquilado")

    def __str__(self):
        return f"Vehiculo(matricula={self.matricula}, modelo={self.modelo}, disponible={self.disponible})"

class Flota:

    def __init__(self):
        self.vehiculos = [] # Lista de objetos/vehiculos

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

if __name__ == '__main__':

    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("MVC-857-C", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("XWG-535-A", "Honda Civic"))

    print("\n[+] Flota Inicial:\n")
    print(flota)

    flota.alquilar_vehiculo("MVC-857-C")

    print("\n[+] Mostrando la flota despues de haber alquilado el Toyota:\n")
    print(flota)

    print("\n[+] Mostrando la flota despues de haber devuelto el Toyota:\n")

    flota.devolver_vehiculo("MVC-857-C")
    print(flota)
    flota.devolver_vehiculo("MVC-857-C")