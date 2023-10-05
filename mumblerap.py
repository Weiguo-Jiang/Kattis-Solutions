N = int(input())
rap = input() + ' '
cur = 0
l = []
for c in rap:
    if not c.isnumeric():
        if l:
            num = int(''.join(l))
            if num > cur:
                cur = num
            l = []
    else:
        l.append(c)
print(cur)
