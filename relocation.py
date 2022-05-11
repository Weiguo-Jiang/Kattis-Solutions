N, Q = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(Q):
	a, b, c = list(map(int, input().split()))
	if a == 1:
		l[b-1] = c
	elif a == 2:
		print(abs(l[b-1]-l[c-1]))
				