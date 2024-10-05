import hashlib
import time
import random
import string

def generate_random_strings(num_strings, min_length=5, max_length=10):
    random_strings = []
    for _ in range(num_strings):
        length = random.randint(min_length, max_length)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        random_strings.append(random_string)
    return random_strings

def compute_hashes(random_strings):
    hash_results = {
        "MD5": {},
        "SHA-1": {},
        "SHA-256": {}
    }
    
    start_time = time.time()
    for s in random_strings:
        hash_value = hashlib.md5(s.encode()).hexdigest()
        hash_results["MD5"][s] = hash_value
    md5_time = time.time() - start_time
    
    start_time = time.time()
    for s in random_strings:
        hash_value = hashlib.sha1(s.encode()).hexdigest()
        hash_results["SHA-1"][s] = hash_value
    sha1_time = time.time() - start_time
    
    start_time = time.time()
    for s in random_strings:
        hash_value = hashlib.sha256(s.encode()).hexdigest()
        hash_results["SHA-256"][s] = hash_value
    sha256_time = time.time() - start_time
    
    return hash_results, md5_time, sha1_time, sha256_time

def detect_collisions(hash_results):
    collisions = {
        "MD5": set(),
        "SHA-1": set(),
        "SHA-256": set()
    }
    
    for algorithm, hashes in hash_results.items():
        seen = {}
        for original_string, hash_value in hashes.items():
            if hash_value in seen:
                collisions[algorithm].add((seen[hash_value], original_string))
            else:
                seen[hash_value] = original_string
                
    return collisions

def main():
    num_strings = random.randint(50, 100)  
    random_strings = generate_random_strings(num_strings)
    
    print(f"Generated {num_strings} random strings.")
    
    hash_results, md5_time, sha1_time, sha256_time = compute_hashes(random_strings)
    
    print(f"MD5 computation time: {md5_time:.6f} seconds")
    print(f"SHA-1 computation time: {sha1_time:.6f} seconds")
    print(f"SHA-256 computation time: {sha256_time:.6f} seconds")
    
    collisions = detect_collisions(hash_results)
    
    for algorithm, collision_pairs in collisions.items():
        if collision_pairs:
            print(f"\nCollisions detected in {algorithm}:")
            for original1, original2 in collision_pairs:
                print(f"Collision: '{original1}' and '{original2}'")
        else:
            print(f"\nNo collisions detected in {algorithm}.")

if __name__ == "__main__":
    main()
