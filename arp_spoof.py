#!/usr/bin/env python3

import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP Scan")
    
    args = parser.parse_args()
    
    return args.target

def main():
    arguments = get_arguments()
    
if __name__ == '__main__':
    main()
        
        