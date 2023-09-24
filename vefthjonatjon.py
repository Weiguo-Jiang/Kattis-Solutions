n = int(input())
d = {'CPU': 0, 'memory': 0, 'hard drive': 0}
for i in range(n):
    a, b, c = input().split()
    a = 0 if a == 'N' else 1
    b = 0 if b == 'N' else 1
    c = 0 if c == 'N' else 1

    d['CPU'] += a
    d['memory'] += b
    d['hard drive'] += c

print(min(d.values()))

