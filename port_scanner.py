#!/usr/bin/env python3

import socket
from termcolor import colored

#host = '10.10.12.254'
#port = 22

host = input("\n[+] Introduce la direccion IP: ")
#port = int(input("\n[+] Introduce el puerto a escanear: "))

def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    
    if s.connect_ex((host, port)):
        print(colored(f"\n[!] El puerto {port} esta cerrado", 'red'))
    else:
        print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
        
    s.close()    
    
def main():
    for port in range(1, 1000):
        port_scanner(port)
    
    
    
if __name__=='__main__':
    main()