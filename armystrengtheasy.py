T = int(input())
for i in range(T):
	blankLine = input()
	NG, NM = list(map(int, input().split()))
	Gozilla = max(list(map(int, input().split())))
	MechaGozilla = max(list(map(int, input().split())))
	if MechaGozilla > Gozilla:
		print("MechaGodzilla")
	elif MechaGozilla <= Gozilla:
		print("Godzilla")