n = int(input())
v = 7
for i in range(n):
	skru = input()
	if skru == 'Skru op!' and v < 10:
		v += 1
	elif skru == 'Skru ned!' and v > 0:
		v -= 1
print(v)