#!/usr/bin/env python3

import socket

def start_udp_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        #s.sendto(b"Hola, aqui estamos tensandola", (host, port))

        #Las siguientes 2 lineasj permiten mandar mensaje con tildes sin crearle conflictos a python para interpretarlas
        message = "Hola, se está tensando muchísimo".encode("utf-8")
        s.sendto(message, (host, port))
        

start_udp_client()