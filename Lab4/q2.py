import random
import time
import logging

def generate_rabin_keys(key_size=1024):
    """Generate public and private keys for Rabin cryptosystem."""
    while True:
        p = random.getrandbits(key_size // 2)
        q = random.getrandbits(key_size // 2)
        if p % 4 == 3 and q % 4 == 3:
            n = p * q
            return (n, p, q)

class KeyManagementService:
    def __init__(self):
        self.keys = {}  
        self.key_logs = []  
    
    def generate_key_for_facility(self, facility_name, key_size=1024):
        public_key, private_key_p, private_key_q = generate_rabin_keys(key_size)
        self.keys[facility_name] = {
            'public_key': public_key,
            'private_key_p': private_key_p,
            'private_key_q': private_key_q,
            'created_at': time.time(),
            'revoked': False
        }
        log_entry = f"Key generated for {facility_name} at {time.ctime()}."
        self.key_logs.append(log_entry)
        logging.info(log_entry)
        print(log_entry)
    
    def distribute_key(self, facility_name):
        if facility_name in self.keys and not self.keys[facility_name]['revoked']:
            return self.keys[facility_name]['public_key'], self.keys[facility_name]['private_key_p'], self.keys[facility_name]['private_key_q']
        else:
            raise Exception(f"Keys for {facility_name} are revoked or do not exist.")
    
    def revoke_key(self, facility_name):
        """Revoke the keys of a facility."""
        if facility_name in self.keys:
            self.keys[facility_name]['revoked'] = True
            log_entry = f"Key revoked for {facility_name} at {time.ctime()}."
            self.key_logs.append(log_entry)
            logging.info(log_entry)
            print(log_entry)
        else:
            raise Exception(f"No keys found for {facility_name}.")
    
    def renew_keys(self, facility_name, key_size=1024):
        if facility_name in self.keys:
            self.generate_key_for_facility(facility_name, key_size)
            log_entry = f"Keys renewed for {facility_name} at {time.ctime()}."
            self.key_logs.append(log_entry)
            logging.info(log_entry)
            print(log_entry)
    
    def log_audit_trail(self):
        for log_entry in self.key_logs:
            print(log_entry)

if __name__ == "__main__":
    logging.basicConfig(filename='key_management.log', level=logging.INFO)

    kms = KeyManagementService()
    kms.generate_key_for_facility("Hospital A")
    public_key, private_key_p, private_key_q = kms.distribute_key("Hospital A")
    print(f"Public Key for Hospital A: {public_key}")
    
    kms.renew_keys("Hospital A")
    kms.revoke_key("Hospital A")
    kms.log_audit_trail()
