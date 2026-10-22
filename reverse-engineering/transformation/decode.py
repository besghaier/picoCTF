with open("enc", "r", encoding="utf-8") as f:
    flag = list(f.read())

print(flag)

decoded = []
for c in flag :
    n = ord(c)
    decoded.append(chr(n >> 8))
    decoded.append(chr(n & 0xFF))

print(''.join(decoded))