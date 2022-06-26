S = [i for i in input()]
P = [i for i in input()]
if P == S:
	print("Yes")
elif len(P)+1 == len(S):
	if S[0].isdigit() or S[-1].isdigit():
		print("Yes")
	else:
		print("No")
elif len(P) == len(S):
	for i in range(len(P)):
		if P[i].isupper():
			P[i] = P[i].lower()
		else:
			P[i] = P[i].upper()
	if P == S:
		print("Yes")
	else:
		print("No")
else:
	print("No")
