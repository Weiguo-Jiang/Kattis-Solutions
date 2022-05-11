P = int(input())
for i in range(P):
	K, N = list(map(int, input().split()))
	print(str(K) + " " + str(int(N*(N+1)/2+N)))