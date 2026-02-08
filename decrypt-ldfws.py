import struct
from Crypto.Cipher import AES
import os

LDFW_COLLECTION = [f for f in os.listdir("LDFWs") if os.path.isfile(os.path.join("LDFWs", f))]

MASTER_KEY = bytes.fromhex("0C9C32D47890FCDA8775DCD388DFEA81A057CBD188A21CAF824337CFAF48182F")
MASTER_IV = bytes.fromhex("DE4C92B1A0C6AE1F79E074FAF844DAA4")

def get_ldfw_decryption_key_iv(ldfw_data):
    key_cipher = AES.new(MASTER_KEY, AES.MODE_CBC, MASTER_IV)
    decrypted_key = key_cipher.decrypt(ldfw_data[0x4c:0x6c])
    iv = bytes(a ^ b for a, b in zip(MASTER_IV, ldfw_data[0xec:0xfc]))
    return decrypted_key, iv

def decrypt_ldfw(ldfw_data, key, iv):
    START = struct.unpack('<I', ldfw_data[0x44:0x48])[0]
    END = struct.unpack('<I', ldfw_data[0x48:0x4C])[0]
    LDFW_CIPHER = AES.new(key, AES.MODE_CBC, iv)

    decrypted_ldfw_block = LDFW_CIPHER.decrypt(ldfw_data[START:END])
    ldfw_data[START:END] = decrypted_ldfw_block
    return

if not os.path.exists("LDFWs/decrypted"):
    os.makedirs("LDFWs/decrypted")

for ldfw in LDFW_COLLECTION:
    ldfw_file_handler = open("LDFWs/" + ldfw, mode="rb")
    ldfw_data = bytearray(ldfw_file_handler.read())
    ldfw_file_handler.close()

    print(f"LDFW: {ldfw}")

    if(ldfw_data[0x28] == 0):
        print(f"Not encrypted")
        dec_ldfw_file_handle = open(f"LDFWs/decrypted/{ldfw}.dec", mode="wb")
        dec_ldfw_file_handle.write(ldfw_data) 
        dec_ldfw_file_handle.close()
        print(f"Saved to LDFWs/decrypted/{ldfw}.dec")
        continue

    key, iv = get_ldfw_decryption_key_iv(ldfw_data)
    print(f"AES Key: {key.hex()}")
    print(f"IV: {iv.hex()}")
    print("Decrypting...")
    decrypt_ldfw(ldfw_data, key, iv)
    dec_ldfw_file_handle = open(f"LDFWs/decrypted/{ldfw}.dec", mode="wb")
    dec_ldfw_file_handle.write(ldfw_data)
    dec_ldfw_file_handle.close()
    print(f"Saved to LDFWs/decrypted/{ldfw}.dec")
    print()
