import random
import time
import rsa
from hashlib import sha256
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding


def diffie_hellman_key_exchange():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())   
    private_key_A = parameters.generate_private_key()
    private_key_B = parameters.generate_private_key()    

    public_key_A = private_key_A.public_key()
    public_key_B = private_key_B.public_key()
    
    shared_key_A = private_key_A.exchange(public_key_B)
    shared_key_B = private_key_B.exchange(public_key_A)
    
    derived_key_A = HKDF(
        algorithm=hashes.SHA256(), length=32, salt=None, info=b"handshake data", backend=default_backend()
    ).derive(shared_key_A)
    
    derived_key_B = HKDF(
        algorithm=hashes.SHA256(), length=32, salt=None, info=b"handshake data", backend=default_backend()
    ).derive(shared_key_B)
    
    assert derived_key_A == derived_key_B, "Key exchange failed!"
    
    return derived_key_A

def generate_rsa_keys():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

def rsa_encrypt(public_key, message):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

def rsa_decrypt(private_key, encrypted_message):
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    return decrypted_message

def rsa_sign(private_key, message):
    return rsa.sign(message.encode(), private_key, 'SHA-256')

def rsa_verify(public_key, message, signature):
    try:
        rsa.verify(message.encode(), signature, public_key)
        return True
    except rsa.VerificationError:
        return False

class KeyManagementSystem:
    def __init__(self):
        self.keys = {}  

    def generate_keys_for_subsystem(self, subsystem_name):
        public_key, private_key = generate_rsa_keys()
        self.keys[subsystem_name] = {'public_key': public_key, 'private_key': private_key}
        print(f"Keys generated for {subsystem_name}.")
    
    def get_public_key(self, subsystem_name):
        return self.keys[subsystem_name]['public_key']
    
    def get_private_key(self, subsystem_name):
        return self.keys[subsystem_name]['private_key']
    
    def revoke_keys(self, subsystem_name):
        if subsystem_name in self.keys:
            del self.keys[subsystem_name]
            print(f"Keys revoked for {subsystem_name}.")
        else:
            print(f"No keys found for {subsystem_name}.")

def secure_communication(subsystem_A, subsystem_B, message, kms):
    print(f"\n=== Secure Communication Between {subsystem_A} and {subsystem_B} ===")
    
    kms.generate_keys_for_subsystem(subsystem_A)
    kms.generate_keys_for_subsystem(subsystem_B)
    
    session_key = diffie_hellman_key_exchange()
    print(f"Session Key: {session_key.hex()}")
    
    public_key_B = kms.get_public_key(subsystem_B)
    encrypted_message = rsa_encrypt(public_key_B, message)
    print(f"Encrypted Message: {encrypted_message}")
    
    private_key_B = kms.get_private_key(subsystem_B)
    decrypted_message = rsa_decrypt(private_key_B, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
    
    private_key_A = kms.get_private_key(subsystem_A)
    signature = rsa_sign(private_key_A, message)
    print(f"Message Signature: {signature}")
    
    public_key_A = kms.get_public_key(subsystem_A)
    if rsa_verify(public_key_A, message, signature):
        print("Signature verified successfully!")
    else:
        print("Signature verification failed!")

if __name__ == "__main__":
    kms = KeyManagementSystem()    
    secure_communication("System A", "System B", "Financial Report", kms)    
    secure_communication("System B", "System C", "Procurement Order", kms)
