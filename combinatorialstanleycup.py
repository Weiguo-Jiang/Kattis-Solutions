N = int(input())
cnt = 0
while N:
	N &= (N-1)
	cnt += 1
print(2**cnt)