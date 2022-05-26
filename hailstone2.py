n = int(input())
cnt = 1
while True:
	if n == 1:
		break
	elif n % 2 == 0:
		n //= 2
	else:
		n = 3*n+1
	cnt += 1
print(cnt)