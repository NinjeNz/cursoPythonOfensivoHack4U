#!/usr/bin/env python3

import tkinter as tk

"""
def accion_de_boton():
    print(f"\n[+] Se ha presionado el boton")

root = tk.Tk()
#root.title("Mi primera APP")
label = tk.Label(root, text="Hola Mundo")
button = tk.Button(root, text="Presioname para que se tense", command=accion_de_boton)
label.pack()
button.pack()
root.mainloop()
"""

root = tk.Tk()
root.title("Metodo pack()")

label1 = tk.Label(root, text="Mi primer label", bg="red")
label2 = tk.Label(root, text="Mi segundo label", bg="green")
label3 = tk.Label(root, text="Mi tercer label", bg="blue")

label1.pack(fill=tk.X)
label2.pack(fill=tk.X)
label3.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()