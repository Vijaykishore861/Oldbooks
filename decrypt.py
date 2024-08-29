from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt(ciphertext, key):
    # Create an AES cipher object with the key and AES.MODE_ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Decrypt the ciphertext and remove the padding
    decrypted_data = cipher.decrypt(unpad(ciphertext), AES.block_size)
    return decrypted_data