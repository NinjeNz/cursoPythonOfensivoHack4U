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
                
    def build_button(self, button, row, col):
        b = tk.Button(self.master, text=button, width=3)
        b.grid(row=row, column=col)

root = tk.Tk() # Ventana principal

my_gui = Calculadora(root) # Instancia de clase

root.mainloop()