n = int(input())
d = dict()
for _ in range(n):
    name = input()
    d[name] = 0

m = int(input())
for _ in range(m):
    line = input().split()[1:]
    for name in line:
        d[name] += 1

l = []
for key, value in d.items():
    l.append((value, key))
l.sort(reverse=True)
for i in l:
    print(i[0], i[1])