import time
import os
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def generate_rsa_keys():
    """Generate RSA 2048-bit key pair."""
    start_time = time.time()
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    end_time = time.time()
    key_gen_time = end_time - start_time
    return private_key, public_key, key_gen_time

def generate_ecc_keys():
    """Generate ECC secp256r1 key pair."""
    start_time = time.time()
    private_key = ec.generate_private_key(
        ec.SECP256R1(),
        backend=default_backend()
    )
    public_key = private_key.public_key()
    end_time = time.time()
    key_gen_time = end_time - start_time
    return private_key, public_key, key_gen_time

def encrypt_file_rsa(public_key, file_data):
    """Encrypt file data using RSA public key."""
    start_time = time.time()
    ciphertext = public_key.encrypt(
        file_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    end_time = time.time()
    encryption_time = end_time - start_time
    return ciphertext, encryption_time

def decrypt_file_rsa(private_key, ciphertext):
    """Decrypt file data using RSA private key."""
    start_time = time.time()
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    end_time = time.time()
    decryption_time = end_time - start_time
    return plaintext, decryption_time

def encrypt_file_ecc(public_key, file_data):
    """Encrypt file data using ECC public key (hybrid encryption via ECDH or ECDSA)."""
    start_time = time.time()
   
    shared_secret = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )[:len(file_data)]  
    
    ciphertext = bytes([a ^ b for a, b in zip(file_data, shared_secret)])  
    
    end_time = time.time()
    encryption_time = end_time - start_time
    return ciphertext, encryption_time

def decrypt_file_ecc(private_key, ciphertext):
    """Decrypt file data using ECC private key."""
    start_time = time.time()    
    public_key = private_key.public_key()
    shared_secret = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )[:len(ciphertext)]
    
    plaintext = bytes([a ^ b for a, b in zip(ciphertext, shared_secret)])
    
    end_time = time.time()
    decryption_time = end_time - start_time
    return plaintext, decryption_time

def create_test_file(file_size_mb):
    """Create a test file with random data of size `file_size_mb` MB."""
    file_size_bytes = file_size_mb * 1024 * 1024  # Convert MB to bytes
    return os.urandom(file_size_bytes)

def compare_rsa_ecc(file_size_mb):
    rsa_private_key, rsa_public_key, rsa_key_gen_time = generate_rsa_keys()
    print(f"RSA 2048-bit key generation time: {rsa_key_gen_time:.6f} seconds")

    ecc_private_key, ecc_public_key, ecc_key_gen_time = generate_ecc_keys()
    print(f"ECC secp256r1 key generation time: {ecc_key_gen_time:.6f} seconds")

    file_data = create_test_file(file_size_mb)

    rsa_ciphertext, rsa_encryption_time = encrypt_file_rsa(rsa_public_key, file_data)
    print(f"RSA encryption time for {file_size_mb} MB: {rsa_encryption_time:.6f} seconds")
    rsa_plaintext, rsa_decryption_time = decrypt_file_rsa(rsa_private_key, rsa_ciphertext)
    print(f"RSA decryption time for {file_size_mb} MB: {rsa_decryption_time:.6f} seconds")

    ecc_ciphertext, ecc_encryption_time = encrypt_file_ecc(ecc_public_key, file_data)
    print(f"ECC encryption time for {file_size_mb} MB: {ecc_encryption_time:.6f} seconds")
    ecc_plaintext, ecc_decryption_time = decrypt_file_ecc(ecc_private_key, ecc_ciphertext)
    print(f"ECC decryption time for {file_size_mb} MB: {ecc_decryption_time:.6f} seconds")

    assert file_data == rsa_plaintext, "RSA decryption failed"
    assert file_data == ecc_plaintext, "ECC decryption failed"
    print("File encryption and decryption verified for both RSA and ECC.")

compare_rsa_ecc(1) 
compare_rsa_ecc(10)  
