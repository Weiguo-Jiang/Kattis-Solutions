n, m = list(map(int, input().split()))
s = set(input().split())
for i in range(n-1):
	ss = set(input().split())
	s &= ss

l = sorted(list(s))
print(len(l))
for i in l:
	print(i)	