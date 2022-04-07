key_public = [11, 221]
key_private = [35, 221]

def encrypt(message):
    encrypted = []
    for i in range(len(message)):
        encrypted.append(pow(ord(message[i]), key_public[0]) % key_public[1])
    return encrypted

def decrypt(encrypted):
    decrypted = ""
    for i in range(len(encrypted)):
        decrypted += chr(pow(encrypted[i], key_private[0]) % key_private[1])
    return decrypted

print(encrypt("Hello"))
print(decrypt(encrypt("Hello")))
