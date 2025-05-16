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

"""
root = tk.Tk()
root.title("Metodo pack()")

label1 = tk.Label(root, text="Mi primer label", bg="red")
label2 = tk.Label(root, text="Mi segundo label", bg="green")
label3 = tk.Label(root, text="Mi tercer label", bg="blue")

label1.pack(fill=tk.X)
label2.pack(fill=tk.X)
#label3.pack(side=tk.LEFT, fill=tk.Y)
label3.pack(side=tk.RIGHT, fill=tk.Y)
#label3.pack(side=tk.BOTTOM, fill=tk.Y)

root.mainloop()
"""
"""
root = tk.Tk()
root.title("Metodo Grid()")

label1 = tk.Label(root, text="Mi primer label", bg="red")
label2 = tk.Label(root, text="Mi segundo label", bg="green")
label3 = tk.Label(root, text="Mi tercer label", bg="blue")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

root.mainloop()
"""
"""
root = tk.Tk()
root.geometry('800x100')
root.title("Metodo Place()")

label1 = tk.Label(root, text="Mi primer label", bg="red")
label2 = tk.Label(root, text="Mi segundo label", bg="green")
label3 = tk.Label(root, text="Mi tercer label", bg="blue")

label1.place(x=20, y=20)
label2.place(relx=0.8, rely=0.2)
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
"""
"""
# ENTRY

root = tk.Tk()
root.geometry('230x100')
root.title("Entry() Widget")

def get_data():
    data = entry_widget.get()
    print(f"\n[+] Datos introducidos por el usuario: {data}")

entry_widget = tk.Entry(root)
entry_widget.pack(pady=5, padx=15, fill=tk.X)

button = tk.Button(root, text="Recoger datos de entrada", command=get_data)
button.pack(padx=15, fill=tk.X)

root.mainloop()
"""
"""
#TEXT

root = tk.Tk()
root.geometry('700x550')
root.title("Text() Widget")

def get_data():
    data = text_widget.get("1.0", tk.END)
    print(f"\n[+] Datos introducidos por el usuario: {data}")

text_widget = tk.Text(root)
text_widget.pack(pady=5, padx=15, fill=tk.X)

button = tk.Button(root, text="Recoger datos de entrada", command=get_data)
button.pack(padx=15, fill=tk.X)

root.mainloop()
"""
"""
# FRAME

root = tk.Tk()
root.geometry('300x200')
root.title("Frame() Widget")

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label1 = tk.Label(frame, text="Esto es un label de prueba", bg="green")
label2 = tk.Label(frame, text="Esto es un label de prueba dos", bg="red")

label1.pack(fill=tk.X)
label2.pack(fill=tk.X)

root.mainloop()
"""

"""
# CANVAS

root = tk.Tk()
root.title("Canvas() Widget")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=15)

oval = canvas.create_oval(50, 50, 150, 150, fill="red")
rect = canvas.create_rectangle(170, 50, 350, 100, fill="green")
line = canvas.create_line(50, 250, 200, 320, fill="blue")

root.mainloop()
"""

# MENU
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Menu() Widget")

def accion_menu():
    messagebox.showinfo("Menu", "Se ha tensado la cosa")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menu", menu=menu1)

menu1.add_command(label="Opcion 1")
menu1.add_command(label="Opcion 2")

menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Extras", menu=menu2)

menu2.add_command(label="Se tensa", command=accion_menu)

root.mainloop()


