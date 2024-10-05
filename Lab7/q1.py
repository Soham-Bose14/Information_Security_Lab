from Crypto.Util import number
import random

def generate_keypair(bits=512):
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    n = p * q
    g = n + 1 
    lambda_n = (p - 1) * (q - 1)  
    mu = number.inverse(lambda_n, n) 
    return (n, g), (lambda_n, mu)

def encrypt(public_key, message):
    n, g = public_key
    r = random.randint(1, n - 1)  
    ciphertext = (pow(g, message, n * n) * pow(r, n, n * n)) % (n * n)
    return ciphertext

def decrypt(private_key, public_key, ciphertext):
    n, _ = public_key
    lambda_n, mu = private_key
    u = pow(ciphertext, lambda_n, n * n)
    l = (u - 1) // n
    message = (l * mu) % n
    return message

def main():
    public_key, private_key = generate_keypair(bits=512)
    a = 15
    b = 25
    ciphertext_a = encrypt(public_key, a)
    ciphertext_b = encrypt(public_key, b)

    ciphertext_sum = (ciphertext_a * ciphertext_b) % (public_key[0] * public_key[0])
    decrypted_sum = decrypt(private_key, public_key, ciphertext_sum)

    print(f"Ciphertext of a: {ciphertext_a}")
    print(f"Ciphertext of b: {ciphertext_b}")
    print(f"Ciphertext of a + b: {ciphertext_sum}")
    print(f"Decrypted sum: {decrypted_sum}")
    print(f"Expected sum: {a + b}")

if __name__ == "__main__":
    main()

