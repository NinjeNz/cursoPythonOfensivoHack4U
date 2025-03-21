# example.txt ("¡Hola mundo!")
"""
# r --> read
# w --> write (escribe borrando lo que ya estaba escrito)
# a --> append (escribe lo que le indiques abajo de lo que ya contenga el archivo)
f = open("example.txt", "a")
f.write("¡Que bonito dia!")
"""
#---------------------------------------------------------------------------------------
# De esta manera python cierra automaticamente el archivo al terminar la ejecucion.
#with open("example.txt", "w") as f:
    #f.write("¡Hola Mundo!")
"""
with open("/etc/hosts", "r") as f:
    file_content = f.read()

print(file_content)"
"""

"""
# Manera mas optima de leer archivos
with open("/etc/hosts", "r") as f:
    for line in f:
        print(line.strip())
"""

"""
with open("/usr/share/wordlists/rockyou.txt", "rb") as f:
    for line in f.readlines():
        print(line.strip().decode())"
"""

"""
mi_lista = ["1 Linea\n", "2 Linea\n", "3 Linea\n", "4 Linea\n"]
with open("example.txt", "w") as f:
    f.writelines(mi_lista)
"""
"""
with open("/usr/share/wordlists/rockyou.txt", "rb") as f:
    first_line = f.readline()

print(first_line)
"""

with open("/home/ninjen/Imágenes/fondo1.jpg", "rb") as f_in, open("image.jpg", "wb") as f_out:
    file_content = f_in.read()
    f_out.write(file_content)