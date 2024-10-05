from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plain_text, key):
    key = key.encode('utf-8')
    
    des = DES.new(key, DES.MODE_ECB)
    
    padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
    
    cipher_text = des.encrypt(padded_text)
    
    return cipher_text

def des_decrypt(cipher_text, key):
    key = key.encode('utf-8')
    des = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = des.decrypt(cipher_text)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size).decode('utf-8')
    
    return decrypted_text

if __name__ == "__main__":
    message = "Confidential Data"
    key = "A1B2C3D4" 
    
    cipher_text = des_encrypt(message, key)
    print(f"Encrypted message: {cipher_text.hex()}")  
    
    decrypted_message = des_decrypt(cipher_text, key)
    print(f"Decrypted message: {decrypted_message}")
