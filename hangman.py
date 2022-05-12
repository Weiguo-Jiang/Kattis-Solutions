w = input()
s = set()
for i in w:
	s.add(i)

a = input()
cnt = 0
for i in a:
	if cnt == 10:
		print("LOSE")
		break
	if len(s) == 0:
		print("WIN")
		break
	if i in s:
		s.remove(i)
	else:
		cnt += 1
