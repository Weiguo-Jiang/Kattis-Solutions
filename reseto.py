def isPrime(n):
	flag = 1
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			flag = 0
			break
	return flag


N, K = list(map(int, input().split()))
l = list()
for i in range(N+1):
	l.append(i)

cnt = 0
P = 2
c = P
while True:
	if P <= N:
		if l[P] != -1:
			l[P] = -1
			cnt += 1
		if cnt == K:
			break
		P += c
	else:
		for i in l:
			if i >= 2 and isPrime(i):
				P = i
				c = P
				break
print(P)
