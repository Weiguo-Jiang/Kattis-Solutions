while True:
	N = int(input())
	if N == 0:
		break

	s = {'aa', 'ee', 'ii', 'oo', 'uu', 'yy'}
	favorite = -1
	maxPair = -1
	for i in range(N):
		word = input()
		cnt = 0
		for j in range(len(word)-1):
			if (word[j]+word[j+1]) in s:
				cnt += 1
		if cnt > maxPair:
			maxPair = cnt
			favorite = word
	print(favorite)