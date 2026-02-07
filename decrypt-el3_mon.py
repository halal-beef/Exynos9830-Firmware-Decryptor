import struct
from Crypto.Cipher import AES

EL3_MON_KEY = bytes.fromhex("9D2DDC5410E693757A74EA025D07173703CCC65A7B5C7B768B099F5FAF065082")
EL3_MON_IV = bytes.fromhex("C421FA6FC8DB9CB22AE2B43BB5671D7F")

EL3_MON_LA = 0xBFE80000
PTR_ENCRYPTION_INFO_OFF = 0x0004

el3_mon_file_handle = open("el3_mon.img", mode="rb")
el3_mon_file = bytearray(el3_mon_file_handle.read())
el3_mon_file_handle.close()

ENCRYPTION_INFO_OFF = struct.unpack("<Q", el3_mon_file[PTR_ENCRYPTION_INFO_OFF:PTR_ENCRYPTION_INFO_OFF + 0x0008])[0]

PTR_ENCRYPTED_REGION_START = (0xBFE8000C - EL3_MON_LA) + ENCRYPTION_INFO_OFF
PTR_ENCRYPTED_REGION_END = (0xBFE80010 - EL3_MON_LA) + ENCRYPTION_INFO_OFF
ENCRYPTED_REGION_START = (struct.unpack("<I", el3_mon_file[PTR_ENCRYPTED_REGION_START:PTR_ENCRYPTED_REGION_START + 0x0004])[0] - EL3_MON_LA)
ENCRYPTED_REGION_END = (struct.unpack("<I", el3_mon_file[PTR_ENCRYPTED_REGION_END:PTR_ENCRYPTED_REGION_END + 0x0004])[0] - EL3_MON_LA)

print(f"EL3 Monitor information:")
print()
print(f"Load address: {hex(EL3_MON_LA)}")
print(f"Encryption info offset: {hex(ENCRYPTION_INFO_OFF)}")
print()
print(f"Encrypted region start: {hex(ENCRYPTED_REGION_START)}")
print(f"Encrypted region end: {hex(ENCRYPTED_REGION_END)}")
print(f"Encrypted region size: {hex(ENCRYPTED_REGION_END - ENCRYPTED_REGION_START)}")
print()
print(f"AES Key: {EL3_MON_KEY.hex()}")
print(f"IV: {EL3_MON_IV.hex()}")
print()
print("Decrypting...")

cipher = AES.new(EL3_MON_KEY, AES.MODE_CBC, EL3_MON_IV)
decrypted_block = cipher.decrypt(el3_mon_file[ENCRYPTED_REGION_START:ENCRYPTED_REGION_END])
el3_mon_file[ENCRYPTED_REGION_START:ENCRYPTED_REGION_END] = decrypted_block

dec_el3_mon_file_handle = open("el3_mon.img.dec", mode="wb")
dec_el3_mon_file_handle.write(el3_mon_file)
dec_el3_mon_file_handle.close()

print("Decrypted version saved to el3_mon.img.dec")
