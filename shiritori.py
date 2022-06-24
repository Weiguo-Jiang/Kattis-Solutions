N = int(input())
flag = 1

s = set()
init = input()
s.add(init)
c = init[-1]
for i in range(N-1):
	w = input()
	if (w[0] != c) or (w in s):
		flag = 0
		if i % 2 == 0:
			print("Player 2 lost")
		else:
			print("Player 1 lost")
		break
	c = w[-1]
	s.add(w)

if flag:
	print("Fair Game")