S = [c for c in input()]
l = [S[0]]
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        l.append(S[i])
print("".join(l))