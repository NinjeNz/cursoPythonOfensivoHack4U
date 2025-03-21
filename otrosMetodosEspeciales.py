"""

# Ejmeplo 1

class Libro:

    def __init__(self, autor, titulo):

        self.autor = autor
        self.titulo = titulo

    def __str__(self):

        return f"El libro '{self.titulo} ha sido escrito por {self.autor}'"
    
    def __eq__(self, otro):

        return self.autor == otro.autor and self.titulo == otro.titulo
    
libro = Libro("Marcelo Vazquez", "¿Como ser un Lammer?")
libro_dos = Libro("Marcelo Vazquez", "¿Como ser un Lammer?")

print(libro)
print(f"¿Son iguales ambos libros? -> {libro == libro_dos}")

"""
"""
# Ejemplo 2

class Caja:

    def __init__(self, *items): # El * indica

        self.items = items

    def mostrar_items(self):

        for item in self.items:
            print(item)

    def __len__(self):

        return len(self.items)        

caja = Caja("Manzana", "Platano", "Kiwi", "Pera", "Mango")

print(len(caja))

"""
"""
# Ejemplo 3

class Pizza:

    def __init__(self, size, *ingredientes):

        self.size = size
        self.ingredientes = ingredientes

    def descripcion(self):

        print(f"Esta pizza tiene {self.size} cm de longitud y los ingredientes son: {', '.join(self.ingredientes)}")

pizza = Pizza(12, "Chorizo", "Jamon", "Tocino", "Queso", "Cebolla")
pizza.descripcion()
"""
"""
# Ejemplo 4

class MiLista:

    def __init__(self):
        self.data = [1, 2 ,3 ,4 ,5]

    def __getitem__(self, index):
        return self.data[index]


lista = MiLista()
print(lista.data[2])

"""
"""
# Ejemplo 5

class Saludo:

    def __init__(self, saludo):
        self.saludo = saludo

    def __call__(self, nombre):

        return f"{self.saludo} {nombre}!"

hola = Saludo("¡Hola")
print(hola("Luis"))
print(hola("Alberto"))
"""
"""
# Ejemplo 6

class Punto:

    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __add__(self, otro):

        return Punto(self.x + otro.x, self.y + otro.y)

    def __str__(self):

        return f"({self.x}, {self.y})"

p1 = Punto(2, 8)
p2 = Punto(10, 65)

print(p1 + p2)
"""

# Ejemplo 7

class Contador:

    def __init__(self, limite):
        self.limite = limite
    
    def __iter__(self):
        self.contador = 0
        return self

    def __next__(self):

        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

c = Contador(15)

for i in c:
    print(i)