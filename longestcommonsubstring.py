n = int(input())
l = []
minLen = 100000
minWord = ''
for i in range(n):
    l.append(input())
    if len(l[i]) < minLen:
        minLen = len(l[i])
        minWord = l[i]

candidates = []
for i in range(minLen):
    for j in range(i, minLen):
        candidates.append(minWord[i:j+1])

for word in l:
    for candidate in candidates:
        if candidate not in word:
            candidates.remove(candidate)

length = 0
for candidate in candidates:
    if len(candidate) > length:
        length = len(candidate)
print(length)