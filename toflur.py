n = int(input())
inp = sorted(list(map(int, input().split())))
s = 0
for i in range(n-1):
	s += (inp[i]-inp[i+1])**2
print(s)
