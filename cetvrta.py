a1, a2 = list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))
c1, c2 = list(map(int, input().split()))
if a1 == b1:
	print(c1, end=" ")
elif a1 == c1:
	print(b1, end=" ")
elif b1 == c1:
	print(a1, end=" ")

if a2 == b2:
	print(c2)
elif a2 == c2:
	print(b2)
elif b2 == c2:
	print(a2)