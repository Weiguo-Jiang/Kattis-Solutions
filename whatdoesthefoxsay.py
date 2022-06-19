T = int(input())
for i in range(T):
	sounds = input().split()
	while True:
		l = input()
		if l == 'what does the fox say?':
			break
		l = l.split()
		for j in range(len(sounds)):
			if sounds[j] == l[-1]:
				sounds[j] = ""
	sounds = [i for i in sounds if i != ""]
	print(" ".join(sounds))