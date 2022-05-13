K = int(input())
N = int(input())
time = 0
for i in range(N):
	T, Z = input().split()
	T = int(T)
	time += T
	if time >= 210:
		print(K)
		break
	if Z == 'T':
		K += 1
		if K == 9:
			K = 1