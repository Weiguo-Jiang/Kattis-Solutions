n = int(input())
cur = input()
if cur[0] != '1':
	print("1")
else:
	correct = "1"
	for i in range(2, n+1):
		correct += str(i)
		if cur[0:len(correct)] != correct:
			print(i)
			break