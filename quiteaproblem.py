while True:
	try:
		inp = input().lower()
	except EOFError:
		break
	if 'problem' in inp:
		print('yes')
	else:
		print('no')