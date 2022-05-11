G, S, C = list(map(int, (input().split())))
s = G*3+S*2+C
flag = 0
if s >= 8:
	print('Province',end=" ")
	flag = 1
elif s >= 5:
	print('Duchy', end=" ")
	flag = 1
elif s >= 2:
	print('Estate', end=" ")
	flag = 1

if flag:
	print('or ', end="")

if s >= 6:
	print('Gold')
elif s >= 3:
	print('Silver')
elif s >= 0:
	print('Copper')