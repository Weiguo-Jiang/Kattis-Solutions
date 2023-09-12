name = input()
p = float(input())
n = int(input())

cnt = 0
for i in range(n):
    if input()[0] == 'e':
        cnt += 1

if cnt > n*p:
    print("Neibb")
else:
    print("Jebb")