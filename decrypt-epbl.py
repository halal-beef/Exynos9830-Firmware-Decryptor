import struct
from Crypto.Cipher import AES

EPBL_KEY = bytes.fromhex("45F5A2F3F2E8C5C234DF481A3D6697FE30244C2F173DC773AC6BDD24087B638E")
EPBL_IV = bytes.fromhex("069F3C80DFBAC1AF5DF0C557712DFE38")

EPBL_LA = 0x02026000

epbl_file_handle = open("epbl.img", mode="rb")
epbl_file = bytearray(epbl_file_handle.read())
epbl_file_handle.close()

PTR_ENCRYPTED_REGION_START = (0x02031D28 - EPBL_LA)
PTR_ENCRYPTED_REGION_END = (0x02031D50 - EPBL_LA)
ENCRYPTED_REGION_START = (struct.unpack("<Q", epbl_file[PTR_ENCRYPTED_REGION_START:PTR_ENCRYPTED_REGION_START + 0x0008])[0] - EPBL_LA)
ENCRYPTED_REGION_END = (struct.unpack("<Q", epbl_file[PTR_ENCRYPTED_REGION_END:PTR_ENCRYPTED_REGION_END + 0x0008])[0] - EPBL_LA)

print(f"EPBL information:")
print()
print(f"Load address: {hex(EPBL_LA)}")
print()
print(f"Encrypted region start: {hex(ENCRYPTED_REGION_START)}")
print(f"Encrypted region end: {hex(ENCRYPTED_REGION_END)}")
print(f"Encrypted region size: {hex(ENCRYPTED_REGION_END - ENCRYPTED_REGION_START)}")
print()
print(f"AES Key: {EPBL_KEY.hex()}")
print(f"IV: {EPBL_IV.hex()}")
print()
print("Decrypting...")

cipher = AES.new(EPBL_KEY, AES.MODE_CBC, EPBL_IV)
decrypted_block = cipher.decrypt(epbl_file[ENCRYPTED_REGION_START:ENCRYPTED_REGION_END])
epbl_file[ENCRYPTED_REGION_START:ENCRYPTED_REGION_END] = decrypted_block

dec_epbl_file_handle = open("epbl.img.dec", mode="wb")
dec_epbl_file_handle.write(epbl_file)
dec_epbl_file_handle.close()

print("Decrypted version saved to epbl.img.dec")
