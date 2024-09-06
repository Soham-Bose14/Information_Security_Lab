def createPlayfairMatrix(key):
    key = key.upper()
    key = key.replace('J', 'I')
    used_chars = set()
    alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    added_alphabets = []
    for c in key:
        if c not in used_chars and c in alphabets:
            added_alphabets.append(c)
            used_chars.add(c)
    for c in alphabets:
        if c not in used_chars:
            added_alphabets.append(c)
            used_chars.add(c)
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(added_alphabets[i:i+5])
    return matrix

def findCharPosition(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None
def playFairCipher(plaintext, key):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace('J', 'I')
    i = 0
    matrix = createPlayfairMatrix(key)
    while i < len(plaintext)-1:
        if plaintext[i] == plaintext[i+1]:
            plaintext.insert(i+1, 'X')
        i += 2
    if len(plaintext) % 2 != 0:
        plaintext.append('X')

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        first = findCharPosition(matrix, plaintext[i])
        second = findCharPosition(matrix, plaintext[i+1])
        if first[0] == second[0]:
            ciphertext += str(matrix[first[0]][(first[1]+1) % 5]) + str(matrix[second[0]][(second[1]+1) % 5])
        elif first[1] == second[1]:
            ciphertext += str(matrix[(first[0]+1) % 5][first[1]]) + str(matrix[(second[0]+1) % 5][second[1]])
        else:
            ciphertext += str(matrix[first[0]][second[1]]) + str(matrix[second[0]][first[1]])

    return ciphertext

def main():
    key = "GUIDANCE"
    message = "The key is hidden under the door pad"
    print(f'Actual Message: {message}')
    encrypted_msg = playFairCipher(message, key)
    print(f'Encrypted Message: {encrypted_msg}')
if __name__ == "__main__":
    main()




































