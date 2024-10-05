import socket
import hashlib

def custom_hash(data):
    hash_value = 5381
    for char in data:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)  
        hash_value &= 0xFFFFFFFF 
    return hash_value

def server_program():
    host = '127.0.0.1' 
    port = 65432 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Server is listening...")

    conn, address = server_socket.accept()
    print(f"Connection from {address} established.")

    data = conn.recv(1024).decode('utf-8')
    print(f"Data received from client: {data}")

    received_hash = custom_hash(data)
    print(f"Computed hash (on server): {received_hash}")

    conn.send(str(received_hash).encode('utf-8'))
    conn.close()

if __name__ == "__main__":
    server_program()
