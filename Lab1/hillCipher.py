import numpy as np

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return -1


def hillCipher(msg, key):
    msg.lower()
    msg.replace(" ", "")
    key = np.array(key)
    key = key.reshape(2,2)
    cipherText = ""
    
    for i in range(0, len(msg), 2):
        p = [ord(msg[i])-97, ord(msg[i+1])-97]
        p = np.array(p)
        c = np.matmul(p,key)
        cipherText += chr((c[0] % 26) + 97) + chr((c[1] % 26) + 97)
    return cipherText

def matrixModInverse(key, mod):
    det = int(np.round(np.linalg.det(key)))
    det_inv = modInverse(det, mod)
    
    if det_inv == -1:
        raise ValueError("Key matrix is not invertible under mod 26")

    adjugate_matrix = np.round(det * np.linalg.inv(key)).astype(int) % mod
    inv_key = (det_inv * adjugate_matrix) % mod

    return inv_key

def hillDecipher(cipherText, key):
    key = np.array(key).reshape(2, 2)    
    inv_key = matrixModInverse(key, 26)
    
    plainText = ""
    
    for i in range(0, len(cipherText), 2):
        p = [ord(cipherText[i])-97, ord(cipherText[i+1])-97]
        p = np.array(p)
        c = np.matmul(p, inv_key) % 26
        
        plainText += chr(int(c[0])+97) + chr(int(c[1])+97)
    
    return plainText

message = "We live in an insecure world"
key = [3,3,2,7]
cipherText = hillCipher(message, key)
print(f'Encrypted message using hill cipher: {cipherText}')
plainText = hillDecipher(cipherText, key)
print(f'Decrypted message using hill cipher: {plainText}')


