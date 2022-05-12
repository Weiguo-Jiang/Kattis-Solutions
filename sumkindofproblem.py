P = int(input())
for i in range(P):
	K, N = list(map(int, input().split()))
	l = [i+1 for i in range(N)]
	odd = [2*i+1 for i in range(N)]
	even = [2*i for i in range(1, N+1)]
	print(str(K) + " " + str(sum(l)) + " " + str(sum(odd)) + " " + str(sum(even)))
