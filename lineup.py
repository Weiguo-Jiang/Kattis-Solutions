n = int(input())
l = list()
for i in range(n):
	name = input()
	l.append(name)

sorted_l = sorted(l)

if l == sorted_l:
	print("INCREASING")
elif l == list(reversed(sorted_l)):
	print("DECREASING")
else:
	print("NEITHER")