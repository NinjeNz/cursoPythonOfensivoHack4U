#!/usr/bin/env python3

import argparse
import subprocess
import signal
#import sys
import os
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo del programa...\n", 'red'))
    #sys.exit(1)
    os._exit(os.EX_OK)
    
signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para descubrir hosts activos en una red (ICMP)")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")
    
    args = parser.parse_args()
    
    return args.target

def parse_target(target_str):
    
    #192.168.1.1-100
    target_str_splitted = target_str.split('.') #["192", "168", "1", "1-100"]
    first_three_octets = '.'.join(target_str_splitted[:3]) # 192.168.1
    
    if len(target_str_splitted) == 4:
        if "-" in target_str_splitted[3]:
            start, end = target_str_splitted[3].split('-')
            return[f"{first_three_octets}.{i}" for i in range(int(start), int(end)+1)]
        else:
            return [target_str]
    else:
        print(colored(f"\n[!] El formato de IP o rango de IP no es valido\n", 'red'))
        
def host_discovery(target):
      
    try:
        ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
            
        if ping.returncode == 0:
            print(colored(f"\t[i] La IP {target} esta activa", 'green'))
    except subprocess.TimeoutExpired:
        pass

def main():
    target_str = get_arguments()
    targets = parse_target(target_str)
    
    print(f"\n[+] Hosts activos en la red:\n")
    
    max_threads = 100
    
    with ThreadPoolExecutor(max_threads) as executor:
        executor.map(host_discovery, targets)
    
    #print(targets)

if __name__ == '__main__':
    main()