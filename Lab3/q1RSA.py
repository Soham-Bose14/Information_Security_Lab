from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def generate_rsa_keys():
    key = RSA.generate(2048)
    
    private_key = key
    public_key = key.publickey()
    
    return public_key, private_key

def rsa_encrypt(plain_text, public_key):
    plain_text_bytes = plain_text.encode('utf-8')
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(plain_text_bytes)
    
    return cipher_text

def rsa_decrypt(cipher_text, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(cipher_text)
    
    return decrypted_text.decode('utf-8')

if __name__ == "__main__":
    public_key, private_key = generate_rsa_keys()
    
    message = "Asymmetric Encryption"
    print(f"Original message: {message}")
    
    cipher_text = rsa_encrypt(message, public_key)
    print(f"Encrypted message (cipher text): {cipher_text.hex()}")  # Display in hexadecimal format
    
    decrypted_message = rsa_decrypt(cipher_text, private_key)
    print(f"Decrypted message: {decrypted_message}")
