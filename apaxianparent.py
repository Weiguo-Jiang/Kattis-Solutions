Y, P = input().split()
if Y[len(Y)-2:len(Y)] == 'ex':
	print(Y+P)
elif Y[-1] == 'e':
	print(Y+'x'+P)
elif Y[-1] == 'a' or Y[-1] == 'i' or Y[-1] == 'o' or Y[-1] == 'u':
	print(Y[:len(Y)-1]+"ex"+P)
else:
	print(Y+"ex"+P)