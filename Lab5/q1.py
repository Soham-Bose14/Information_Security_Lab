def custom_hash(input_string):
    hash_value = 5381
    for char in input_string:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)  
        hash_value &= 0xFFFFFFFF  
    return hash_value

if __name__ == "__main__":
    input_string = "Hello, World!"
    hash_result = custom_hash(input_string)
    print(f"The hash value for '{input_string}' is: {hash_result}")
