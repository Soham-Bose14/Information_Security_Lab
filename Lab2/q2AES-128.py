from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plain_text, key):
    key = key[:16].encode('utf-8')
    iv = get_random_bytes(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    
    return iv + cipher_text

def aes_decrypt(cipher_text, key):
    key = key[:16].encode('utf-8')
    iv = cipher_text[:16]
    cipher_text = cipher_text[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(cipher_text)
    decrypted_text = unpad(decrypted_padded_text, AES.block_size).decode('utf-8')
    
    return decrypted_text

if __name__ == "__main__":
    message = "Sensitive Information"
    key = "0123456789ABCDEF0123456789ABCDEF"  
    cipher_text = aes_encrypt(message, key)
    print(f"Encrypted message: {cipher_text.hex()}") 
    decrypted_message = aes_decrypt(cipher_text, key)
    print(f"Decrypted message: {decrypted_message}")
