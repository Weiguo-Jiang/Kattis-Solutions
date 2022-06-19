T = int(input())
cnt = 1
for i in range(T):
	n = int(input())
	v1 = sorted(list(map(int, input().split())))
	v1.reverse()
	v2 = sorted(list(map(int, input().split())))
	s = 0
	for j in range(n):
		s += v1[j]*v2[j]
	print("Case #" + str(cnt) + ": " + str(s))
	cnt += 1