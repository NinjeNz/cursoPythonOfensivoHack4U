#!/usr/bin/env python3

class Libro:

    def __init__(self, id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self): # Metodo especial
        return f"Libro({self.id_libro}, {self.autor}, {self.nombre_libro})"
    
    def __repr__(self):
        return self.__str__()
    
class Biblioteca:

    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
        else:
            print(f"\n[!] No es posible agregar el libro con ID {libro.id_libro}")

    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]


if __name__ == '__main__':

    biblioteca = Biblioteca()

    libro1 = Libro(1, "Marcelo Vazquez", "¿Como ser un Lammer de Potencia Maxima?")
    libro2 = Libro(2, "Pepito Manolete", "Aprende a colorear desde cero")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")