from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.number import inverse

def generate_keypair(nlength=1024):
    key = RSA.generate(nlength)
    pub_key = key.publickey()
    return pub_key, key

def encrypt(pub_key, message):
    e = pub_key.e
    n = pub_key.n
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypt(priv_key, ciphertext):
    d = priv_key.d
    n = priv_key.n
    message = pow(ciphertext, d, n)
    return message

def main():
    pub_key, priv_key = generate_keypair()
    a = 7
    b = 3
    ciphertext_a = encrypt(pub_key, a)
    ciphertext_b = encrypt(pub_key, b)

    ciphertext_product = (ciphertext_a * ciphertext_b) % pub_key.n

    decrypted_product = decrypt(priv_key, ciphertext_product)

    print(f"Ciphertext of a: {ciphertext_a}")
    print(f"Ciphertext of b: {ciphertext_b}")
    print(f"Ciphertext of a * b: {ciphertext_product}")
    print(f"Decrypted product: {decrypted_product}")
    print(f"Expected product: {a * b}")

if __name__ == "__main__":
    main()

