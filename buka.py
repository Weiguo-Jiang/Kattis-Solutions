A = input()
o = input()
B = input()
if o == '*':
	print('1' + '0'*(len(A)+len(B)-2))
else:
	if len(A) == len(B):
		print('2' + '0'*(len(A)-1))
	else:
		print('1' + '0'*(max(len(A), len(B))-min(len(A), len(B))-1) + '1' + '0'*(min(len(A), len(B))-1))