"""
nombre = input("\nCual es tu nombre?: ")
print(f"\n Gracias {nombre}")

while True:

    try:
        edad = int(input("\n Cual es tu edad?: "))
        print(f"\n Perfecto, el año que viene deberias cumplir {edad+1} años")
        break
    except ValueError:
        print(f"\n[!] El tipo de dato introducido es incorrecto")
"""

# Utilizando el modulo getpass el cual no muestra lo que estas escribiendo

from getpass import getpass

password = getpass(f"\n Escribe tu contraseña: ")
print(f"\n Tu contraseña es: {password}")