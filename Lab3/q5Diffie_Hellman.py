import time
import random

def mod_exp(base, exp, mod):
    """Efficient modular exponentiation using the square-and-multiply method."""
    return pow(base, exp, mod)

def generate_dh_key_pair(p, g):
    """Generates a Diffie-Hellman private and public key pair."""
    private_key = random.randint(2, p - 2)  
    public_key = mod_exp(g, private_key, p) 
    return private_key, public_key

def compute_shared_secret(their_public_key, my_private_key, p):
    """Computes the shared secret using the other peer's public key and my private key."""
    shared_secret = mod_exp(their_public_key, my_private_key, p)  
    return shared_secret

p = 23 
g = 5

def diffie_hellman_key_exchange():
    print("=== Diffie-Hellman Key Exchange ===")

    start_time = time.time()
    private_key_a, public_key_a = generate_dh_key_pair(p, g)
    key_gen_time_a = time.time() - start_time
    print(f"Peer A's Public Key: {public_key_a}, Private Key: {private_key_a}")
    print(f"Key Generation Time for Peer A: {key_gen_time_a:.6f} seconds")

    start_time = time.time()
    private_key_b, public_key_b = generate_dh_key_pair(p, g)
    key_gen_time_b = time.time() - start_time
    print(f"Peer B's Public Key: {public_key_b}, Private Key: {private_key_b}")
    print(f"Key Generation Time for Peer B: {key_gen_time_b:.6f} seconds")

    start_time = time.time()
    shared_secret_a = compute_shared_secret(public_key_b, private_key_a, p)
    key_exchange_time_a = time.time() - start_time

    start_time = time.time()
    shared_secret_b = compute_shared_secret(public_key_a, private_key_b, p)
    key_exchange_time_b = time.time() - start_time

    assert shared_secret_a == shared_secret_b, "Key exchange failed! Secrets do not match."
    print(f"Shared Secret: {shared_secret_a}")
    
    print(f"Key Exchange Time for Peer A: {key_exchange_time_a:.6f} seconds")
    print(f"Key Exchange Time for Peer B: {key_exchange_time_b:.6f} seconds")
    return key_gen_time_a, key_gen_time_b, key_exchange_time_a, key_exchange_time_b

if __name__ == "__main__":
    diffie_hellman_key_exchange()
