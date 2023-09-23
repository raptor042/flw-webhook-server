from rsa import PublicKey, PrivateKey, decrypt

def loadKeyPair():
    with open("keys/public.pem", "rb") as file:
        pubKey = PublicKey.load_pkcs1(file.read())
    with open("keys/private.pem", "rb") as file:
        secKey = PrivateKey.load_pkcs1(file.read())

    return (pubKey, secKey)

def decrypt_data(data, key):
    cipherText = bytes.fromhex(data)
    text = decrypt(cipherText, key).decode("ascii")

    return text