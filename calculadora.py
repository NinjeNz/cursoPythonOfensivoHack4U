#!/use/bin/env python3

import tkinter as tk

class Calculadora:

    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="#ef1111", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        
        row = 1
        col = 0
        
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "="
            
        ]
        
        for button in buttons:
            self.build_button(button, row, col)
            col += 1
            
            if col > 3:
                col = 0
                row += 1
    
    def clear_display(self):
        self.display.delete(0, "end") # Tambien puede usarse 'tk.END' en lugar de "end", el efecto es el mismo.
        
    def calculate(self):
        print(f"\n[+] Este metodo aun no ha sido implementado\n")
        
    def click(self, key): # key es el button que se esta presionando
        self.display.insert("end", key) # Con "end" indicamos que los valores se inserten desde el final.
        print(f"\n[+] Has presionado el boton {key}")
               
    def build_button(self, button, row, col):
        if button == "C":
            b = tk.Button(self.master, text=button, width=3, command=lambda: self.clear_display())
        elif button == "=":
            b = tk.Button(self.master, text=button, width=3, command=lambda: self.calculate())
        else:
            b = tk.Button(self.master, text=button, width=3, command=lambda: self.click(button)) # Usamos funciones lambda para asegurarnos no llamar la funcion hasta hacer click a pesar de los parentesis.
            
        b.grid(row=row, column=col)

root = tk.Tk() # Ventana principal

my_gui = Calculadora(root) # Instancia de clase

root.mainloop()