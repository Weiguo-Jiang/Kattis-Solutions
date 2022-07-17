from math import ceil
Q, M, S, L = list(map(int, input().split()))
if M == 1:
	print(Q*L+S)
else:
	if S == 0:
		print(ceil(L/M)*Q)
	elif L == 0:
		print(ceil(S/M))
	else:
		r = ceil(L/M)
		mod = L%M
		if mod == 0:
			print(r*Q+ceil(S/M))
		else:
			gap = (M-mod)*Q
			if S <= gap:
				print(r*Q)
			else:
				S -= gap
				print(r*Q+ceil(S/M))