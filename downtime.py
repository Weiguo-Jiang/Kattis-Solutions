ll = list()

def binarySearch(num, l, h):
	while l < h:
		m = (l+h)//2
		if ll[m] >= num:
			h = m
		else:
			l = m + 1

	if ll[l] < num:
		return l
	else:
		return l-1


def main():
	n, k = list(map(int, input().split()))
	for i in range(n):
		ll.append(int(input()))

	cnt = -1
	for i in range(n):
		index = binarySearch(ll[i]+1000, i, n-1)
		if index - i + 1 > cnt:
			cnt = index - i + 1
	
	if cnt % k == 0:
		print(cnt//k)
	else:
		print(cnt//k+1)


if __name__ == '__main__':
	main()