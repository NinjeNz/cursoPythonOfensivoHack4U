import os
import shutil

"""if os.path.exists("mi_archivo.txt"):
    print(f"\n[+] El archivo existe\n")
else:
    print(f"\n[!] El archivo no existe\n")"""

"""if not os.path.exists("mi_directorio"):
    os.mkdir("mi_directorio")"""

"""if not os.path.exists("mi_directorio/mi_subdirectorio"):
    os.makedirs("mi_directorio/mi_subdirectorio")"""

"""
# Ejecute en linux la siguiente linea para crear 5 archivos consecutivos : for i in $(seq 1 5); do touch file$i.txt; done
#Despues ejecutar el script de python
print(f"\n[+] Listando todos los recursos del directorio actual de trabajo:\n")
recursos = os.listdir()

for recurso in recursos:
    print(recurso)"""

    
"""if os.path.exists("file1.txt"):
    os.remove("file1.txt")"""

"""if os.path.exists("mi_directorio"):
    shutil.rmtree("mi_directorio")"""


"""if os.path.exists("file2.txt"):
    os.rename("file2.txt", "cambiado.txt")"""

"""if os.path.exists("/etc/passwd"):
    tamaño = os.path.getsize("/etc/passwd")

print(f"\n[+] El archivo /etc/ pesa {tamaño} bytes")"""

ruta = os.path.join("mi_directorio", "mi_archivo.txt")
print(f"\n[+] Ruta: {ruta}")

archivo = os.path.basename(ruta)

print(f"\n[+] Nombre del archivo: {archivo}")

#directorio = os.path.dirname(ruta)
directorio, archivo = os.path.split(ruta)

#print(f"\n[+] Nombre del directorio donde esta contenido el archivo: {directorio}")
print(f"\n[+] Archivo: {archivo}, Directorio: {directorio}")
