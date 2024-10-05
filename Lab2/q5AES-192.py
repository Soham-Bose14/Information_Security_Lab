from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def aes_192_encrypt(plain_text, key):
    key = key.encode('utf-8')
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    
    return iv + cipher_text 

if __name__ == "__main__":
    message = "Top Secret Data"
    key = "FEDCBA9876543210FEDCBA9876543210" 
    cipher_text = aes_192_encrypt(message, key[:24]) 
    print(f"Encrypted message (hex): {cipher_text.hex()}")  
