import socket
import hashlib

def compute_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 65432)
    server_socket.bind(server_address)

    server_socket.listen(1)
    print("Server is listening on port 65432...")

    while True:
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")

            message_parts = []
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                message_parts.append(data.decode())

            full_message = ''.join(message_parts)
            print(f"Received message: {full_message}")

            message_hash = compute_hash(full_message)
            print(f"Computed hash: {message_hash}")
            connection.sendall(message_hash.encode())
        
        finally:
            connection.close()

if __name__ == "__main__":
    main()
