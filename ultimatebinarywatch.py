def binary(d, l):
	cnt = 0
	while d != 0:
		mod = d%2
		d //= 2
		if mod == 1:
			l[cnt] = '*'
		cnt += 1

def main():
	s = input()
	l1 = ['.', '.', '.', '.']
	l2 = ['.', '.', '.', '.']
	l3 = ['.', '.', '.', '.']
	l4 = ['.', '.', '.', '.']

	binary(int(s[0]), l1)
	binary(int(s[1]), l2)
	binary(int(s[2]), l3)
	binary(int(s[3]), l4)

	for i in range(3, -1, -1):
		print(l1[i] + " " + l2[i] + "   " + l3[i] + " " + l4[i])

if __name__ == "__main__":
	main()
