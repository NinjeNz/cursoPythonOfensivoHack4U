class Libro:

    IVA = 0.21

    def __init__(self, titulo, autor, precio):
        
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod # Decorador que permite operar con los argumentos sin tomar en cuenta el objeto (self)
    def es_bestseller(total_ventas):

        return total_ventas > 5000
        
    @staticmethod
    def precio_con_iva(precio):
        return precio + precio * Libro.IVA

    def precio_con_iva2(self):
        return self.precio + self.precio * Libro.IVA
    
    @classmethod
    def precio_con_ivacls(cls, precio):
        return precio + precio * cls.IVA

class LibroDigital(Libro): #Se aplica herencia al pasarle como parametro la clase Libro
    IVA = 0.10

mi_libro = Libro("¿Como ser un Lammer de verdad", "Marcelo Vazquez", 17.5)
mi_libro_digital = LibroDigital("Iniciacion al Lammer", "Marcelo Vazquez", 17.5)
print(Libro.es_bestseller(8000))
# print con @statickmethod
print(f"\n[+] El precio del libro con IVA incluido es de {round(Libro.precio_con_iva(mi_libro.precio),2)}") #Round sirve para redondear
#print usando self en metodo precio_con_iva2
print(f"\n[+] El precio del libro con IVA incluido es de {mi_libro.precio_con_iva2()}")
# Haciendo uso de @classmethod
print(f"\n El precio del libro digital con IVA incluido es de {LibroDigital.precio_con_ivacls(mi_libro_digital.precio)}")

# NOTA: Si usaramos staticmethod en el anterior print