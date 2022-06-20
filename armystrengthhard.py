T = int(input())
for i in range(T):
	blank = input()
	NG, NM = input()
	maxG = max(list(map(int, input().split())))
	maxM = max(list(map(int, input().split())))

	if maxG >= maxM:
		print("Godzilla")
	else:
		print("MechaGodzilla")