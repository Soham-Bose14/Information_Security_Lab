from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def triple_des_encrypt(plain_text, key):
    key = key[:24].encode('utf-8')
    iv = get_random_bytes(8)  
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_text = pad(plain_text.encode('utf-8'), DES3.block_size)
    cipher_text = cipher.encrypt(padded_text)
    
    return iv + cipher_text  

def triple_des_decrypt(cipher_text, key):
    key = key[:24].encode('utf-8')
    iv = cipher_text[:8]
    cipher_text = cipher_text[8:]
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(cipher_text)
    decrypted_text = unpad(decrypted_padded_text, DES3.block_size).decode('utf-8')
    
    return decrypted_text

if __name__ == "__main__":
    message = "Classified Text"
    key = "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"  
    
    cipher_text = triple_des_encrypt(message, key)
    print(f"Encrypted message: {cipher_text.hex()}")  
    
    decrypted_message = triple_des_decrypt(cipher_text, key)
    print(f"Decrypted message: {decrypted_message}")
