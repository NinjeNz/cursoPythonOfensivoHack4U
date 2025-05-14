"""
import threading
import time

def tarea(num_tarea):
    print(f"\n[+] Tarea {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Tarea {num_tarea} finalizando")

# Definimos los hilos y le pasamos la funcion que debe ejecutar junto con sus argumentos
thread1 = threading.Thread(target=tarea, args=(1, ))
thread2 = threading.Thread(target=tarea, args=(2, ))

# Ejecucion de los hilos
thread1.start()
thread2.start()

# Con Join esperamos a que los hilos en ejecucion terminen antes de realizar ejecuciones posteriores como el print de abajo.
thread1.join()
thread2.join()

print(f"\n[+] Los hilos han finalizado exitosamente")
"""

### Ejemplos usando threading ###
"""
# Sin threading
import threading
import time
import requests

dominios = [
    "https://google.com.mx",
    "https://xvideos.com",
    "https://wikipedia.org",
    "https://yahoo.com"
]

start_time = time.time()

for url in dominios:
    response = requests.get(url)
    print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

end_time = time.time()

print(f"\n[+] Tiempo total transcurrido: {end_time - start_time}")

"""
# Con threading

import threading
import time
import requests

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

dominios = [
    "https://google.com.mx",
    "https://xvideos.com",
    "https://wikipedia.org",
    "https://yahoo.com"
]

start_time = time.time()

hilos = []
for url in dominios:
    hilo = threading.Thread(target=realizar_peticion, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

end_time = time.time()

print(f"\n[+] Tiempo total transcurrido: {round(end_time - start_time, 2)} segundos")