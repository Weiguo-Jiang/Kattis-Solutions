n = int(input())
for i in range(n):
	n, post, birth, c = input().split()
	flag = 0
	if int(c) <= 40:
		flag = 0.5
	if int(post.split('/')[0]) >= 2010:
		flag = 1
	if int(birth.split('/')[0]) >= 1991:
		flag = 1
	if flag == 1:
		print(n + " " + "eligible")
	elif flag == 0.5:
		print(n + " " + "coach petitions")
	else:
		print(n + " " + "ineligible")