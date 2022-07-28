from math import gcd

def printFraction(num, deno):
	if num < 0 and deno < 0:
		num *= -1
		deno *= -1
		print(str(num)+' / '+str(deno))
	elif num < 0:
		num *= -1
		print('-'+str(num)+' / '+str(deno))
	elif deno < 0:
		deno *= -1
		print('-'+str(num)+' / '+str(deno))
	else:
		print(str(num)+' / '+str(deno))


def reduceFraction(num, deno):
	c = gcd(num, deno)
	num //= c
	deno //= c
	if num == 0:
		deno = 1
	printFraction(num, deno)


n = int(input())
for i in range(n):
	op = input().split()
	x1, y1, op, x2, y2 = int(op[0]), int(op[1]), op[2], int(op[3]), int(op[4])

	if op == '+':
		deno = y1*y2
		num = x1*y2+x2*y1
		reduceFraction(num, deno)
	elif op == '-':
		deno = y1*y2
		num = x1*y2-x2*y1
		reduceFraction(num, deno)
	elif op == '/':
		deno = x2*y1
		num = x1*y2
		reduceFraction(num, deno)
	else:
		deno = y1*y2
		num = x1*x2
		reduceFraction(num, deno)
