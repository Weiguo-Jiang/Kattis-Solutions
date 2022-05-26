def attack(A, B, C, D, n):
	flag1 = 0
	flag2 = 0

	mod1 = n % (A+B)
	mod2 = n % (C+D)
	if mod1 <= A and mod1 != 0:
		flag1 = 1
	if mod2 <= C and mod2 != 0:
		flag2 = 1
	if flag1 + flag2 == 0:
		print("none")
	elif flag1 + flag2 == 1:
		print("one")
	else:
		print("both")


def main():
	A, B, C, D = list(map(int, input().split()))
	P, M, G = list(map(int, input().split()))

	attack(A, B, C, D, P)
	attack(A, B, C, D, M)
	attack(A, B, C, D, G)

if __name__ == "__main__":
	main()