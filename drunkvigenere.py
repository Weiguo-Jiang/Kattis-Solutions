msg = [c for c in input()]
key = [c for c in input()]

for i in range(len(key)):
    if i % 2 == 0:
        key[i] = ord(key[i]) - 65
    else:
        key[i] = -(ord(key[i]) - 65)

for i in range(len(msg)):
    ascii = ord(msg[i])-key[i]
    if ascii < 65:
        ascii += 26
    elif ascii > 90:
        ascii -= 26
    msg[i] = chr(ascii)

print(''.join(msg))
