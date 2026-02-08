import struct
from Crypto.Cipher import AES
import os

MASTER_KEY = bytes.fromhex("E83420592B7FC371C6734501C767D38E982C6584B1518E1C450A362A57F1C50E")
MASTER_IV = bytes.fromhex("C3471249DDF13D50180AB6C8A9589294")

def get_tzsw_decryption_key(tzsw_data):
    key_cipher = AES.new(MASTER_KEY, AES.MODE_CBC, MASTER_IV)
    decrypted_key = key_cipher.decrypt(tzsw_data[0x40:0x60])
    return decrypted_key

def decrypt_tzsw(tzsw_data, key, iv):
    START = struct.unpack('<I', tzsw_data[0x28:0x2c])[0]
    END = struct.unpack('<I', tzsw_data[0x2c:0x30])[0]
    TZSW_CIPHER = AES.new(key, AES.MODE_CBC, iv)

    decrypted_tzsw_block = TZSW_CIPHER.decrypt(tzsw_data[START:END])
    tzsw_data[START:END] = decrypted_tzsw_block
    return

tzsw_file_handler = open("tzsw.img", mode="rb")
tzsw_data = bytearray(tzsw_file_handler.read())
tzsw_file_handler.close()

key = get_tzsw_decryption_key(tzsw_data)
iv = tzsw_data[0x60:0x70]

print(f"AES Key: {key.hex()}")
print(f"IV: {iv.hex()}")
print("Decrypting...")
decrypt_tzsw(tzsw_data, key, iv)
dec_tzsw_file_handle = open(f"tzsw.img.dec", mode="wb")
dec_tzsw_file_handle.write(tzsw_data)
dec_tzsw_file_handle.close()
print("Decrypted version saved to tzsw.img.dec")
print()
