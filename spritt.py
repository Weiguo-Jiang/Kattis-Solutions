n, x = map(int, input().split())
s = 0
for i in range(n):
    s += int(input())

if x >= s:
    print("Jebb")
else:
    print("Neibb")