#!/usr/bin/env python3

import scapy.all as scapy
import argparse
import subprocess
import signal
#import sys
import os
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP Scan")
    
    args = parser.parse_args()
    
    return args.target

def scan(ip):
    #scapy.arping(ip)
    
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_packet = broadcast_packet/arp_packet
    
    answered, unanswered = scapy.srp(arp_packet, timeout=1, verbose=False)
    
    response = answered.summary()
    if response:
        print(response)
        
    #print(answered)
    print(unanswered)
    
def main():
    target = get_arguments()
    scan(target)
    
    
if __name__ == '__main__':
    main()