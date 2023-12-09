d1 = dict()
for i in range(26):
    d1[chr(i+65)] = i

d2 = dict()
for i in range(26):
    d2[i] = chr(i+65)

digits = [int(x) for x in input()]
n = int(input())
for _ in range(n):
    message = input()
    mapping = [d1[message[i]] * digits[i] % 26 for i in range(len(digits))]
    print(''.join([d2[x] for x in mapping]))