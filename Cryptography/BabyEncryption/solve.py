def decryption(msg):
    ct = []
    modInv = pow(123, -1, 256)
    for char in msg:
        ct.append((modInv * (char - 18)) % 256)
    return bytes(ct)

enc = bytes.fromhex(open('msg.enc', 'r').read())
print(decryption(enc))