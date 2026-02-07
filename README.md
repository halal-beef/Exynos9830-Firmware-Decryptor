# Exynos9830 Firmware Decryptor

Collection of scripts to decrypt parts of the firmware for Exynos9830

>[!CAUTION]
> These scripts will only work on Exynos9830 images, don't try these for other SoCs unless you have the right keys and IV for them.

## How to run

- Install requirements via ```pip3 install -r requirements.txt```
- Place encrypted epbl.img and el3_mon.img into the same folder
- Run decryptors via ```python3 decrypt-el3_mon.py``` and ```decrypt-epbl.py```
- Finished

## Example output

```
❯ python3 decrypt-el3_mon.py 
EL3 Monitor information:

Load address: 0xbfe80000
Encryption info offset: 0x328

Encrypted region start: 0x540
Encrypted region end: 0x14780
Encrypted region size: 0x14240

AES Key: 9d2ddc5410e693757a74ea025d07173703ccc65a7b5c7b768b099f5faf065082
IV: c421fa6fc8db9cb22ae2b43bb5671d7f

Decrypting...
Decrypted version saved to el3_mon.img.dec

~/decryptors
❯ python3 decrypt-epbl.py
EPBL information:

Load address: 0x2026000

Encrypted region start: 0x16d0
Encrypted region end: 0xbcb0
Encrypted region size: 0xa5e0

AES Key: 45f5a2f3f2e8c5c234df481a3d6697fe30244c2f173dc773ac6bdd24087b638e
IV: 069f3c80dfbac1af5df0c557712dfe38

Decrypting...
Decrypted version saved to epbl.img.dec
```

## TODO

- [ ] Extract key and IV for LDFW

