import uuid
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

BLOCK_SIZE = 32

def encrypt(plaintext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the plaintext and encrypt it
    ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
    return ciphertext

def secret_key():
   secret_key1 = uuid.uuid4()
   skey = str(secret_key1)[:BLOCK_SIZE]
   return skey

secret_key1 = secret_key()

def message_skey(message):
   message1 = message.encode("utf8")
   encrypted_message = encrypt(message1,secret_key().encode("utf8"))
   return str(encrypted_message)

