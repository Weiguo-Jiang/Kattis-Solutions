n = int(input())
for i in range(n):
	l = input().lower()
	s = set()
	for j in range(ord('a'), ord('z')):
		s.add(chr(j))
	s.add('z')

	ans = list()
	for j in l:
		try:
			s.remove(j)
		except KeyError:
			flag = 0

	for i in s:
		ans.append(i)

	if len(ans) == 0:
		print("pangram")
	else:
		ans = sorted(ans)
		print("missing " + "".join(ans))
