n = int(input())
for i in range(n):
	a = int("".join(input().split()))
	b = int("".join(input().split()))
	ans = [i for i in str(a+b)]
	print(" ".join(ans))