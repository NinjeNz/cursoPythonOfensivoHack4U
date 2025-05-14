import multiprocessing
import time

def tarea(num_tarea):
    print(f"\n[+] Proceso {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Proceso {num_tarea} finalizando")

# Definimos los procesos y le pasamos la funcion que debe ejecutar junto con sus argumentos
proceso1 = multiprocessing.Process(target=tarea, args=(1, ))
proceso2 = multiprocessing.Process(target=tarea, args=(2, ))

# Ejecucion de los procesos
proceso1.start()
proceso2.start()

# Con Join esperamos a que los procesos en ejecucion terminen antes de realizar ejecuciones posteriores como el print de abajo.
proceso1.join()
proceso2.join()

print(f"\n[+] Los procesos han finalizado exitosamente")