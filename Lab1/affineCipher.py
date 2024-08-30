def additive_cipher(msg, key):
    encrypted_msg = ""
    for ch in msg:
        if not ch.isalpha():
            encrypted_msg += ch
            continue
        start = 65 if ch.isupper() else 97
        pos = ord(ch) - start
        new_pos = (pos + key) % 26
        encrypted_msg += chr(new_pos + start)
    return encrypted_msg

def decrypt_additive_cipher(msg, key):
    decrypted_msg = ""
    for ch in msg:
        if not ch.isalpha():
            decrypted_msg += ch
            continue
        start = 65 if ch.isupper() else 97
        pos = ord(ch) - start
        new_pos = (pos - key) % 26
        decrypted_msg += chr(new_pos + start)
    return decrypted_msg

def multiplicative_cipher(msg, key):
    encrypted_msg = ""
    for ch in msg:
        if not ch.isalpha():
            encrypted_msg += ch
            continue
        start = 65 if ch.isupper() else 97
        pos = ord(ch) - start
        new_pos = (pos * key) % 26
        encrypted_msg += chr(new_pos + start)
    return encrypted_msg

def modular_inverse(num, m):
    for x in range(1, m):
        if (num * x) % m == 1:
            return x
    return 0

def decrypt_multiplicative_cipher(msg, key):
    decrypted_msg = ""
    a_inverse = modular_inverse(key, 26)
    if a_inverse == 0:
        raise ValueError("No modular inverse exists for the given key.")
    for ch in msg:
        if not ch.isalpha():
            decrypted_msg += ch
            continue
        start = 65 if ch.isupper() else 97
        pos = ord(ch) - start
        new_pos = (pos * a_inverse) % 26
        decrypted_msg += chr(new_pos + start)
    return decrypted_msg

def affine_cipher(msg, key):
    encrypted_msg = ""
    for ch in msg:
        if not ch.isalpha():
            encrypted_msg += ch
            continue
        start = 65 if ch.isupper() else 97
        pos = ord(ch) - start
        new_pos = (pos * key[0] + key[1]) % 26
        encrypted_msg += chr(new_pos + start)
    return encrypted_msg

def decrypt_affine_cipher(msg, key):
    decrypted_msg = ""
    a_inverse = modular_inverse(key[0], 26)
    if a_inverse == 0:
        raise ValueError("No modular inverse exists for the given key.")
    for ch in msg:
        if not ch.isalpha():
            decrypted_msg += ch
            continue
        start = 65 if ch.isupper() else 97
        pos = ord(ch) - start
        new_pos = (a_inverse * (pos - key[1])) % 26
        decrypted_msg += chr(new_pos + start)
    return decrypted_msg

msg = "I am learning information security"
print(f'Message to be encrypted: {msg}\n')

key = 20
print(f'Encrypted message using additive cipher: {additive_cipher(msg, key)}')

key = 15
print(f'Encrypted message using multiplicative cipher: {multiplicative_cipher(msg, key)}')

affine_key = (15, 20)
print(f'Encrypted message using affine cipher: {affine_cipher(msg, affine_key)}\n')

print(f'Decrypted message using additive cipher: {decrypt_additive_cipher(additive_cipher(msg, key), key)}')
print(f'Decrypted message using multiplicative cipher: {decrypt_multiplicative_cipher(multiplicative_cipher(msg, key), key)}')
print(f'Decrypted message using affine cipher: {decrypt_affine_cipher(affine_cipher(msg, affine_key), affine_key)}\n')
