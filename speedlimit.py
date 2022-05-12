while True:
	n = int(input())
	if n == -1:
		break
	miles = 0
	s = 0
	t = 0
	for i in range(n):
		s1, t1 = list(map(int, input().split()))
		miles += (t1-t)*s1
		s = s1
		t = t1
	print(str(miles) + " miles")