N = int(input())
TB = 0
LR = 0
for i in range(N):
	inp = input()
	if inp[0] == '0':
		TB += 1
	if inp[1] == '0':
		TB += 1
	if inp[2] == '0':
		LR += 1
	if inp[3] == '0':
		LR += 1

n = min(TB, LR) // 2
print(n, end=" ")

TB -= n * 2
print(TB, end=" ")

LR -= n * 2
print(LR)