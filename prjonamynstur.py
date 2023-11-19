d = dict()
d['.'] = 20
d['O'] = 10
d['\\'] = 25
d['/'] = 25
d['A'] = 35
d['^'] = 5
d['v'] = 22

n, m = map(int, input().split())
s = 0
for i in range(n):
    s += sum([d[x] for x in input()])
print(s)