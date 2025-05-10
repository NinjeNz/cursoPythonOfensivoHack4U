#!/usr/bin/env python3

import sys

print(f"\n[+] Nombre del script: {sys.argv[0]}")
print(f"[+] Total de argumentos que se estan pasando al programa: {len(sys.argv)}")
print(f"[+] Mostrando el primer argumento: {sys.argv[1]}")
print(f"[+] Mostrando el segundo argumento: {sys.argv[2]}")
print(f"[+] Mostrando el todos los argumentos: {', '.join(argument for argument in sys.argv)}")

print(f"\n[+] Mostrando las rutas de Python:\n")

for element in sys.path:
    print(element)


print(f"\n[+] Saliendo con un codigo de estado 1 (no exitoso)")
sys.exit(1)