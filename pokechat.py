S = input()
d = dict()
for i in range(len(S)):
    d[i+1] = S[i]

ids = input()
l = list()
for i in range(0, len(ids), 3):
    l.append(d[int(ids[i:i+3])])

print("".join(l))