import socket
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

p, g, B = map(int, client_socket.recv(1024).decode().split(","))

a = random.randint(1, p - 2)
A = pow(g, a, p)

client_socket.send(str(A).encode())

shared_secret_client = pow(B, a, p)
print(f"Client's Shared Secret: {shared_secret_client}")

client_socket.close()

