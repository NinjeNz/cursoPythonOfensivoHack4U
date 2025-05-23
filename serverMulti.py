import socket
import threading

def server_program():
    
    host = 'localhost'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT
    server_socket.bind((host, port))
    server_socket.listen()
    
    print(f"\n[+] El servidor está en escucha de conexiones entrantes...")
    
    clients = []
    usernames = {}





if __name__ == '__main__':
    server_program()