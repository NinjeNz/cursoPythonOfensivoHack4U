#!/usr/bin/env python3

"""
import socket
import argparse 
from termcolor import colored
import sys

#host = '10.10.12.254'
#port = 22

#host = input("\n[+] Introduce la direccion IP: ")
#port = int(input("\n[+] Introduce el puerto a escanear: "))

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", help="Victim target to scan (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", help="Port range to scan (Ex: -p 1-100)")
    options = parser.parse_args()
    
    if options.target is None or options.port is None:
        parser.print_help()
        sys.exit(1)
        
    return options.target, options.port
        

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    return s

def port_scanner(port, host, s):
    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
        s.close() 
        
    except (socket.timeout, ConnectionRefusedError):
        #print(colored(f"\n[!] El puerto {port} esta cerrado", 'red'))
        s.close()
        #pass
            
def main():
    
    target, port = get_arguments()
    
    if '-' in port:
        ports = port.split('-')
        
    
        for port in range(int(ports[0]), int(ports[1])):
            s = create_socket()
            port_scanner(port, target, s)
    
    elif ',' in port:
        ports = port.split(',')
        
        for port in ports:
            s = create_socket()
            port_scanner(int(port), target, s)
    
    
if __name__=='__main__':
    main()
"""

# Mismo programa pero optimizado

"""
import socket
import argparse 
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim target to scan (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range to scan (Ex: -p 1-100)")
    options = parser.parse_args()
    
    #if options.target is None or options.port is None:
    #    parser.print_help()
    #    sys.exit(1)
        
    return options.target, options.port
        
def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    return s

def port_scanner(port, host, s):
    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
        s.close() 
        
    except (socket.timeout, ConnectionRefusedError):
        s.close()
        #pass

def scan_ports(ports, target):
    for port in ports:
        s = create_socket()
        port_scanner(port, target, s)

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)
    
def main():
    
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target) 
    
if __name__=='__main__':
    main()
"""

# Refactorizado utilizando threading

"""
import socket
import argparse 
import threading
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim target to scan (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range to scan (Ex: -p 1-100)")
    options = parser.parse_args()
    
    #if options.target is None or options.port is None:
    #    parser.print_help()
    #    sys.exit(1)
        
    return options.target, options.port
        
def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    return s

def port_scanner(port, host):
    s = create_socket()
    
    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
        s.close() 
        
    except (socket.timeout, ConnectionRefusedError):
        s.close()
        #pass

def scan_ports(ports, target):
    threads = []
    for port in ports:
        thread = threading.Thread(target=port_scanner, args=(port, target))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)
    
def main():
    
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target) 
    
if __name__=='__main__':
    main()
"""

# Usando ThreadPoolExecutor y Signal

import socket
import argparse
import signal
#import sys
import os
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

open_sockets = []

def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo del programa...", 'red'))
    
    for socket in open_sockets:
        socket.close()
        
    #sys.exit(1) #En mi caso no funciono, investigar el porque....
    os._exit(os.EX_OK)
    
signal.signal(signal.SIGINT, def_handler) # Ctrl+c

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim target to scan (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range to scan (Ex: -p 1-100)")
    options = parser.parse_args()
    
    #if options.target is None or options.port is None:
    #    parser.print_help()
    #    sys.exit(1)
        
    return options.target, options.port
        
def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    open_sockets.append(s)
    return s

def port_scanner(port, host):
    s = create_socket()
    
    try:
        s.connect((host, port))
        s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
        response = s.recv(1024)
        #response = response.decode(errors='ignore').split('\n')[0]
        response = response.decode(errors='ignore').split('\n')
        
        if response:
            print(colored(f"\n[+] El puerto {port} esta abierto\n", 'green'))
            
            for line in response:
                print(colored(f"{line}", 'yellow'))
        else:
            print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
        
    except (socket.timeout, ConnectionRefusedError):
        pass
    
    finally:
        s.close()

def scan_ports(ports, target):
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)
        
def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)
    
def main():
    
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target) 
    
if __name__=='__main__':
    main()