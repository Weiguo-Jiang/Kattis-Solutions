def sum(l, h):
	s = 0
	for i in range(l, h):
		s += i
	return s

n = int(input())
even = 0
odd = 0

for i in range(1, 100-n+2):
	s = sum(i, i+n)
	if s % 2 == 0:
		even = 1
	if s % 2 == 1:
		odd = 1
if even == 1 and odd == 1:
	print("Either")
elif even == 1:
	print("Even")
else:
	print("Odd")