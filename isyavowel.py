inp = input()
cnt = 0
cnty = 0
for c in inp:
    if c in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
        cnty += 1

    if c == 'y':
        cnty += 1

print("{0} {1}".format(cnt, cnty))