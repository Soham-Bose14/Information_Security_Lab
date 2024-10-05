import random

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def generate_elgamal_keys(p):
    g = 2  
    x = random.randint(1, p - 2)    
    h = mod_exp(g, x, p)
    
    return (p, g, h), x 

def pad_message(plain_text):
    while len(plain_text) % 16 != 0:
        plain_text += ' '
    return plain_text

def elgamal_encrypt(plain_text, public_key):
    p, g, h = public_key
    padded_text = pad_message(plain_text)
    m = int.from_bytes(padded_text.encode('utf-8'), byteorder='big')
    
    if m >= p:
        raise ValueError("Message is too large for the chosen prime modulus.")
    
    y = random.randint(1, p - 2)    
    c1 = mod_exp(g, y, p)
    c2 = (m * mod_exp(h, y, p)) % p
    
    return c1, c2

def elgamal_decrypt(cipher_text, private_key, p):
    c1, c2 = cipher_text    
    s = mod_exp(c1, private_key, p)
    
    try:
        s_inv = pow(s, -1, p)  
    except ValueError:
        raise ValueError("Error: Modular inverse does not exist")
    
    m = (c2 * s_inv) % p    
    decrypted_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
    
    try:
        decrypted_message = decrypted_bytes.decode('utf-8').rstrip()
    except UnicodeDecodeError as e:
        raise ValueError(f"Decryption failed: {e}")
    
    return decrypted_message

if __name__ == "__main__": 
    p = 340282366920938463463374607431768211507 
    public_key, private_key = generate_elgamal_keys(p)    
    message = "Confidential Data"
    cipher_text = ""
    print(f"Original message: {message}")
    
    try:
        cipher_text = elgamal_encrypt(message, public_key)
        print(f"Encrypted message (cipher text): {cipher_text}")
    except ValueError as e:
        print(e)
    
    try:
        decrypted_message = elgamal_decrypt(cipher_text, private_key, p)
        print(f"Decrypted message: {decrypted_message}")
    except ValueError as e:
        print(e)
