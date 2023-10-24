l = []
d = {}

while True:
    try:
        first, last = input().split()
    except EOFError:
        break

    l.append((last, first))
    if first in d:
        d[first] += 1
    else:
        d[first] = 1

l.sort()
for i in l:
    if d[i[1]] > 1:
        print(i[1], i[0])
    else:
        print(i[1])
