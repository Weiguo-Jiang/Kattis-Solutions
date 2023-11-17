m = int(input())
n = int(input())
cnt = 0
for _ in range(n):
    cnt += input().count('.')
print(cnt/m/n)