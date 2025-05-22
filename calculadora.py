#!/use/bin/env python3

import tkinter as tk

class Calculadora:

    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="#ef1111", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = 0
        
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

        self.master.bind("<Key>", self.key_press)
        
    def key_press(self, event):
        key = event.char
        
        if key == "\r": # Representa la tecla Enter, la usamos para accionar el boton "="
            self.calculate()
            return
        elif key == "\x08": # Representa la tecla Backspace, la usamos para limpiar la pantalla
            self.clear_display()
            return
        elif key == "\x1b": # Representa la tecla Escape, la usamos para cerrar la calculadora
            self.master.quit()
            return
            
        self.click(key)
        
    def clear_display(self):
        self.display.delete(0, "end") # Tambien puede usarse 'tk.END' en lugar de "end", el efecto es el mismo.
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = 0
        
    def calculate(self):
        
        if self.current and self.op:
            if self.op =="/":
                self.total /= float(self.current)
            if self.op =="*":
                self.total *= float(self.current)
            if self.op =="+":
                self.total += float(self.current)
            if self.op =="-":
                self.total -= float(self.current)
                
        self.display.delete(0, "end")
        self.display.insert("end", round(self.total, 3))
        
    def click(self, key): # key es el button que se esta presionando
        
        if self.op_verification:
            self.op_verification = False
        
        self.display.insert("end", key) # Con "end" indicamos que los valores se inserten desde el final.
        
        if key in "0123456789" or key == ".":
            self.current += key
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)
                    
            self.current = ''
            self.op_verification = True
            self.op = key
        
        #print(f"\n[+] Has presionado el boton {key}")
        #print(f"[+] La primera combinacion es: {self.current}")
        #print(f"[+] Status op_verification: {self.op_verification}")
        #print(f"[+] Operacion a realizar: {self.op}")
        #print(f"[+] Total: {self.total}")
               
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
