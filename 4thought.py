operators = ['+', '-', '*', '//']
possibleValues = dict()
for i in operators:
	for j in operators:
		for k in operators:
			expr = "4 {0} 4 {1} 4 {2} 4".format(i, j, k)
			val = eval(expr)
			l = expr.split()
			for m in range(len(l)):
				if l[m] == '//':
					l[m] = '/'
			expr = " ".join(l)
			possibleValues[val] = expr

m = int(input())
for i in range(m):
	n = int(input())
	if n in possibleValues:
		print(possibleValues[n], end="")
		print(" = " + str(n))
	else:
		print("no solution")