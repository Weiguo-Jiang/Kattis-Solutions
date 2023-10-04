d = dict()
for i in range(26):
    d[chr(i+65)] = i
d['_'] = 26
d['.'] = 27

dd = dict()
for k, v in d.items():
    dd[v] = k

while True:
    line = input()
    if line == '0':
        break

    N, msg = line.split()
    N = int(N)
    msg = [c for c in msg[::-1]]
    for i in range(len(msg)):
        msg[i] = dd[(d[msg[i]]+N)%28]
    print(''.join(msg))