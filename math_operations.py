# Este es un modulo que se llamara desde diferentes scripts.

def suma(x, y):
    return x + y

def resta(x, y):
    return x -y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("[!] No es posible dividir un numero entre cero")
    else:
        return x / y