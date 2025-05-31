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