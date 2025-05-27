import socket
import threading

def client_thread(client_socket, clients, usernames):
    print(f"\n[+] Estamos en client_thread")
    
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username
    
    #print(usernames)
    print(f"\n[+] El usuario {username} se ha conectado al chat")
    
    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] El usuario {username} ha entrado al chat\n\n".encode())
            
            
    while True:
        try:
            message = client_socket.recv(10124).decode()
            
            if not message:
                break
            
            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())
        except:
            break

def server_program():
    
    host = 'localhost'
    port = 12346
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT
    server_socket.bind((host, port))
    server_socket.listen()
    
    print(f"\n[+] El servidor está en escucha de conexiones entrantes...")
    
    clients = []
    usernames = {}


    while True:
        
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        
        print(f"\n[+] Se ha conectado un nuevo cliente: {address}")
        
        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()
        
    server_socket.close()


if __name__ == '__main__':
    server_program()