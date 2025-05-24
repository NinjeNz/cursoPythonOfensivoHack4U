#!/usr/bin/env python3

import socket 
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def send_message(event, client_socket, username, text_widget, entry_widget):
     message = entry_widget.get()
     client_socket.sendall(f"{username} > {message}".encode())
     
     entry_widget.delete(0, END)
     text_widget.configure(state='normal')
     text_widget.insert(END, f"{username} > {message}\n")
     text_widget.configure(state='disabled')

def client_program():
    
     host = 'localhost'
     port = 12345
     
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client_socket.connect((host, port))
     
     username = input(f"\n[+] Introduce tu usuario: ")
     client_socket.sendall(username.encode())
     
     window = Tk()
     window.title("Chat")
     
     
     text_widget = ScrolledText(window, state='disabled')
     text_widget.pack(padx=5, pady=5)
     
     entry_widget = Entry(window)
     entry_widget.bind("<Return>", lambda event: send_message(event, client_socket, username, text_widget, entry_widget))
     entry_widget.pack(padx=5, pady=5, fill=BOTH, expand=1)
     
     
     window.mainloop()
     client_socket.close()
     
if __name__ == '__main__':
    client_program()    