N, M = list(map(int, input().split()))
inp = [int(i) for i in input().split()]
p = 0
cnt = 0
for i in inp:
	p += i
	if p > N:
		break
	cnt += 1
print(M-cnt)