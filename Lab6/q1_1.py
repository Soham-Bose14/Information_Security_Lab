from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from Crypto.Util.number import GCD

key = ElGamal.generate(256, get_random_bytes)
public_key = (int(key.p), int(key.g), int(key.y))  
private_key = int(key.x) 

def elgamal_encrypt(message, key):
    p, g, y = int(key.p), int(key.g), int(key.y)  
    k = randint(1, p - 2)
    while GCD(k, p - 1) != 1:
        k = randint(1, p - 2)
    c1 = pow(g, k, p)
    c2 = (message * pow(y, k, p)) % p
    return (c1, c2)

def elgamal_decrypt(cipher_text, key):
    c1, c2 = cipher_text
    p = int(key.p)  
    s = pow(c1, int(key.x), p) 
    s_inv = pow(s, p - 2, p)  
    return (c2 * s_inv) % p


message = 4441
cipher_text = elgamal_encrypt(message, key)
decrypted_message = elgamal_decrypt(cipher_text, key)

print("Original message:", message)
print("Encrypted message:", cipher_text)
print("Decrypted message:", decrypted_message)

