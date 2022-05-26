def recur(n):
	global cnt
	if n == 0:
		cnt += 1
	elif n < 0:
		return
	else:
		recur(n-1)
		recur(n-2)
		recur(n-3)

cnt = 0
n = int(input())
recur(n)
print(cnt)