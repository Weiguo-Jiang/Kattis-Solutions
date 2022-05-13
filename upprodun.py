N = int(input())
M = int(input())
if M%N == 0:
	for i in range(N):
		print('*'*(M//N))
else:
	d = (M//N+1)*N-M
	for i in range(d):
		print('*'*(M//N))
	for i in range(N-d):
		print('*'*(M//N+1))