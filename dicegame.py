a1, b1, a2, b2 = list(map(int, input().split()))
a3, b3, a4, b4 = list(map(int, input().split()))
sum1 = 0
cnt1 = 0
for i in range(a1, b1+1):
	for j in range(a2, b2+1):
		sum1 += i+j
		cnt1 += 1

sum2 = 0
cnt2 = 0
for i in range(a3, b3+1):
	for j in range(a4, b4+1):
		sum2 += i+j
		cnt2 += 1

avg1 = sum1/cnt1
avg2 = sum2/cnt2

if avg1 > avg2:
	print("Gunnar")
elif avg1 < avg2:
	print("Emma")
else:
	print("Tie")