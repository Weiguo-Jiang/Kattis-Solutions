d = dict()
d['c'] = [2, 3, 4, 7, 8, 9, 10]
d['d'] = [2, 3, 4, 7, 8, 9]
d['e'] = [2, 3, 4, 7, 8]
d['f'] = [2, 3, 4, 7]
d['g'] = [2, 3, 4]
d['a'] = [2, 3]
d['b'] = [2]
d['C'] = [3]
d['D'] = [1, 2, 3, 4, 7, 8, 9]
d['E'] = [1, 2, 3, 4, 7, 8]
d['F'] = [1, 2, 3, 4, 7]
d['G'] = [1, 2, 3, 4]
d['A'] = [1, 2, 3]
d['B'] = [1, 2]

n = int(input())
for i in range(n):
    l = [c for c in input()]
    cnt = [0]*10
    if len(l) == 0:
        print(' '.join([str(c) for c in cnt]))
        continue
    last = d[l[0]]
    for c in last:
        cnt[c-1] += 1

    for c in l[1:]:
        cur = d[c]
        for j in cur:
            cnt[j-1] += 1 if j not in last else 0
        last = cur

    cnt = [str(c) for c in cnt]
    print(' '.join(cnt))