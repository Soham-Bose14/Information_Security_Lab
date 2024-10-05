from ecies import encrypt, decrypt
from ecies.utils import generate_key

def generate_ecc_keys():
    private_key = generate_key()
    public_key = private_key.public_key.format(True)
    
    return public_key, private_key

def ecc_encrypt(plain_text, public_key):
    plain_text_bytes = plain_text.encode('utf-8')    
    cipher_text = encrypt(public_key, plain_text_bytes)
    
    return cipher_text

def ecc_decrypt(cipher_text, private_key):
    decrypted_text = decrypt(private_key.secret, cipher_text)
    
    return decrypted_text.decode('utf-8')

if __name__ == "__main__":
    public_key, private_key = generate_ecc_keys()
    
    message = "Secure Transactions"
    print(f"Original message: {message}")
    
    cipher_text = ecc_encrypt(message, public_key)
    print(f"Encrypted message (cipher text): {cipher_text.hex()}") 
    
    decrypted_message = ecc_decrypt(cipher_text, private_key)
    print(f"Decrypted message: {decrypted_message}")
