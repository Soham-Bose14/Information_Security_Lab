def vigenere_cipher(msg, key):
    encrypted_msg = ""
    msg = msg.lower()
    keyInd = 0
    for i in range(len(msg)):
        if not msg[i].isalpha():
            continue
        pos = (ord(msg[i])-97 + ord(key[keyInd % len(key)])-97) % 26
        encrypted_msg += chr(pos+97)
    return encrypted_msg

def decrypt_vigenere_cipher(encrypted_msg, key):
    encrypted_msg = encrypted_msg.lower()
    decrypted_msg = ""
    keyInd = 0
    for i in range(len(encrypted_msg)):
        pos = (ord(encrypted_msg[i]) - 97 + 26 - ord(key[keyInd % len(key)]) + 97) % 26
        decrypted_msg += chr(pos+97)
    return decrypted_msg


key = "dollars"
message = "the house is being sold tonight"
print(f'Message to be encypted: {message}')
cipherText = vigenere_cipher(message, key)
print(f'Encrypted message using vigenere cipher: {cipherText}')
plainText = decrypt_vigenere_cipher(cipherText, key)
print(f'Decrypted message using vigenere cipher: {plainText}')
