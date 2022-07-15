d = dict()
d[1] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
d[2] = {2, 3, 5, 6, 8, 9, 0}
d[3] = {3, 6, 9}
d[4] = {4, 5, 6, 7, 8, 9, 0}
d[5] = {5, 6, 8, 9, 0}
d[6] = {6, 9}
d[7] = {7, 8, 9, 0}
d[8] = {8, 9, 0}
d[9] = {9}
d[0] = {0}


def valid(l):
	s = d[l[0]]
	for i in range(1, len(l)):
		if l[i] in s:
			s = d[l[i]]
		else:
			return 0
	return 1


def main():
	T = int(input())
	for i in range(T):
		k = int(input())
		d = 0
		while True:
			larger = [int(c) for c in str(k+d)]
			smaller = [int(c) for c in str(k-d)]

			if valid(larger):
				print(k+d)
				break

			if valid(smaller):
				print(k-d)
				break

			d += 1



if __name__ == '__main__':
	main()