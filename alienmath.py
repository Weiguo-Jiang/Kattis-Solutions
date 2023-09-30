B = int(input())
key = input().split()
s = set(key)
d = dict()
for i in range(B):
    d[key[i]] = i

digits = []
parse = input()
ptr1 = 0
ptr2 = 0
while True:
    if ptr1 == len(parse):
        break

    sub = parse[ptr1:ptr2+1]

    if sub in s:
        digits.append(d[sub])
        ptr1 = ptr2 + 1
        ptr2 = ptr1
    else:
        ptr2 += 1

digits.reverse()

ans = 0
base = 1
for i in digits:
    ans += i * base
    base *= B

print(ans)