import socket
import hashlib

def custom_hash(data):
    hash_value = 5381
    for char in data:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)  
        hash_value &= 0xFFFFFFFF  
    return hash_value

def client_program():
    host = '127.0.0.1' 
    port = 65432  

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = "Hello from the client!"
    client_socket.send(message.encode('utf-8'))

    local_hash = custom_hash(message)
    print(f"Computed hash (on client): {local_hash}")

    received_hash = int(client_socket.recv(1024).decode('utf-8'))
    print(f"Hash received from server: {received_hash}")

    if local_hash == received_hash:
        print("Data integrity verified! No corruption or tampering.")
    else:
        print("Data corruption or tampering detected!")

    client_socket.close()

if __name__ == "__main__":
    client_program()
