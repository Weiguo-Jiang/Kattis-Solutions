n, p = map(int, input().split())
d1 = dict()
d1['c'] = ['number of', 'most', 'fewest', 'more', 'fewer', 'many', 'few']
d1['m'] = ['amount of', 'most', 'least', 'more', 'less', 'much', 'little']

d2 = dict()
for _ in range(n):
    noun, type = input().split()
    d2[noun] = type

for _ in range(p):
    inp = input().split()
    noun = inp[-1]
    type = d2[noun]
    if " ".join(inp[:-1]) in d1[type]:
        print("Correct!")
    else:
        print("Not on my watch!")