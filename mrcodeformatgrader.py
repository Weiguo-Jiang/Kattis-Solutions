C, N = list(map(int, input().split()))
l = [int(i) for i in input().split()]
l.append(-1)
ll = list()
for i in range(1, C+1):
	if i not in l:
		ll.append(i)
ll.append(-1)

errors = list()
start = l[0]
end = l[0]
for i in range(1, N+1):
	if l[i] == end + 1:
		end = l[i]
	else:
		if start == end:
			errors.append(str(end))
		else:
			errors.append(str(start) + '-' + str(end))
		start = l[i]
		end = l[i]
print("Errors: ", end="")
if len(errors) == 1:
	print(errors[-1])
else:
	for i in range(len(errors)-2):
		print(errors[i], end=", ")
	print(errors[-2], end=" and ")
	print(errors[-1])

correct = list()
start = ll[0]
end = ll[0]
for i in range(1, len(ll)):
	if ll[i] == end + 1:
		end = ll[i]
	else:
		if start == end:
			correct.append(str(end))
		else:
			correct.append(str(start) + '-' + str(end))
		start = ll[i]
		end = ll[i]
print("Correct: ", end="")
if len(correct) == 1:
	print(correct[-1])
else:
	for i in range(len(correct)-2):
		print(correct[i], end=", ")
	print(correct[-2], end=" and ")
	print(correct[-1])
