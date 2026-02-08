# Exynos9830 Firmware Decryptor

Collection of scripts to decrypt parts of the firmware for Exynos9830

>[!CAUTION]
> These scripts will only work on Exynos9830 images, don't try these for other SoCs unless you have the right keys and IV for them.

## How to run

- Install requirements via ```pip3 install -r requirements.txt```
- Place encrypted epbl.img and el3_mon.img into the same folder
- Place LDFW fragments into the ```LDFWs``` folder
- Run decryptors via ```python3 decrypt-el3_mon.py```, ```python3 decrypt-epbl.py``` and ```python3 decrypt-ldfws.py```
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

~/decryptors
❯ python decrypt-ldfws.py
LDFW: CryptoManagerV50.ldfw
AES Key: 4b88bd5d1d337319caa166f5220ad9e8166f1944600d7ae6598ff940fb21d774
IV: f37ca59c90f78e2e4eda40cbd80f89f0
Decrypting...
Saved to LDFWs/decrypted/CryptoManagerV50.ldfw.dec

LDFW: drm_fw.ldfw
AES Key: b05206fe2994b49234f9401ba0b39026a48eff05a5922df12ee0ee0c38ad727d
IV: f37ca59c90f78e2e4eda40c8d80f89f0
Decrypting...
Saved to LDFWs/decrypted/drm_fw.ldfw.dec

LDFW: fmp_fw_V20.ldfw
AES Key: 80a37f57ab8e881f417a609dce3d34b5ae9ada755ef53b3e6e3f19b1ca9a4d26
IV: f37ca59c90f78e2e4eda40c8d80f89f0
Decrypting...
Saved to LDFWs/decrypted/fmp_fw_V20.ldfw.dec

LDFW: hdcp_fw.ldfw
AES Key: 9d18814f9e2ca0a1f4bb01fcbffcdde8a74829315068cb931a2b015f49dd1407
IV: f37ca59c90f78e2e4eda40c8d80f89f0
Decrypting...
Saved to LDFWs/decrypted/hdcp_fw.ldfw.dec

LDFW: srpmb_fw.ldfw
AES Key: 782c9e76c5e39324b126bbd702f6215fada27bec00d820d73282c11135618cd1
IV: f37ca59c90f78e2e4eda40c8d80f89f0
Decrypting...
Saved to LDFWs/decrypted/srpmb_fw.ldfw.dec

LDFW: tail_fw.ldfw
Not encrypted
Saved to LDFWs/decrypted/tail_fw.ldfw.dec
```

## Notes

- Encrypted LDFW fragments can be extracted using [my tool](https://github.com/halal-beef/ldfw-extractor)

## TODO

- [x] Extract key and IV for LDFW

