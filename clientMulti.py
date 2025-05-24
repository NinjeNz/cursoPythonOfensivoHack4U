#!/usr/bin/env python3

import socket 
import threading

def client_program():
    
     host = 'localhost'
     port = 12345
     
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client_socket.connect((host, port))
     
     username = input(f"\n[+] Introduce tu usuario: ")
     client_socket.sendall(username.encode())
     
if __name__ == '__main__':
    client_program()    