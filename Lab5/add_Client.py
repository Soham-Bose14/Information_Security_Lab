import socket
import hashlib

def compute_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 65432)
    client_socket.connect(server_address)

    try:
        original_message = "This is a test message sent in multiple parts."
        message_parts = [original_message[i:i+10] for i in range(0, len(original_message), 10)]
        
        for part in message_parts:
            client_socket.sendall(part.encode())

        client_socket.shutdown(socket.SHUT_WR)

        hash_from_server = client_socket.recv(1024).decode()
        print(f"Received hash from server: {hash_from_server}")

        local_hash = compute_hash(original_message)
        print(f"Local hash: {local_hash}")

        if hash_from_server == local_hash:
            print("Message integrity verified!")
        else:
            print("Message integrity verification failed!")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
