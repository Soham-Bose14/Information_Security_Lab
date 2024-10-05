import socket
import random
from sympy import isprime


def generate_large_prime(bits=256):
    return next(n for n in iter(lambda: random.getrandbits(bits), None) if isprime(n))


p = generate_large_prime()
g = random.randint(2, p - 2)

b = random.randint(1, p - 2)
B = pow(g, b, p)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
print("Server listening on port 12345...")

client_socket, addr = server_socket.accept()
print(f"Connected to client: {addr}")

client_socket.send(f"{p},{g},{B}".encode())

A = int(client_socket.recv(1024).decode())

shared_secret_server = pow(A, b, p)
print(f"Server's Shared Secret: {shared_secret_server}")

client_socket.close()
server_socket.close()

