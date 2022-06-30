case = 1
while True:
	inp = input()
	if inp == 'END':
		break
	cnt = 0
	for i in inp[1:]:
		if i == '.':
			cnt += 1
		else:
			break

	if cnt == 0 and inp == '*'*len(inp):
		print(str(case) + " EVEN")
	elif cnt == 0 and inp != '*'*len(inp):
		print(str(case) + " NOT EVEN")
	else:
		split = cnt*'.'

		l = inp.split(split)

		flag = 1

		for i in l:
			if i != '*':
				print(str(case) + " NOT EVEN")
				flag = 0
				break
		if flag:
			print(str(case) + " EVEN")
	case += 1