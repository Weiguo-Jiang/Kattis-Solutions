#
# BEGIN-HEADER
#
# Name: Weiguo Jiang
#
# Student-ID: 1670913
#
# By submitting this code, you are agreeing that you have solved in accordance
# with the collaboration policy in CMPUT 303/403.
#
# END-HEADER
#


d = dict()
dd = dict()
while True:
	try:
		inp = input().split()
	except EOFError:
		break

	if inp[0] == 'def':
		if inp[1] in d:
			del dd[int(d[inp[1]])]
		d[inp[1]] = inp[2]
		dd[int(inp[2])] = inp[1]
	elif inp[0] == 'clear':
		d = dict()
		dd = dict()
	else:
		l = list()
		eq = inp[1:]
		flag = 0
		for i in eq:
			if i == '=':
				break
			elif i == '+' or  i == '-':
				l.append(i)
			elif i in d:
				l.append(d[i])
			else:
				flag = 1
				break

		if flag:
			print(" ".join(eq)+" unknown")
		else:
			ans = eval(" ".join(l))
			if ans in dd:
				print(" ".join(eq) + " " + dd[ans])
			else:
				print(" ".join(eq)+" unknown")

