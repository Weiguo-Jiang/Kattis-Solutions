N = int(input())
bev = input()
for i in range(N, 1, -1):
	if i == 2:
		print("2 bottles of " + bev + " on the wall, " + "2 bottles of " + bev +".")
		print("Take one down, pass it around, " + "1 bottle of " + bev + " on the wall.")
	else:
		print(str(i) + " bottles of " + bev + " on the wall, " + str(i) + " bottles of " + bev +".")
		print("Take one down, pass it around, " + str(i-1) + " bottles of " + bev + " on the wall.")

print("1 bottle of " + bev + " on the wall, " + "1 bottle of " + bev +".")
print("Take it down, pass it around, " + "no more bottles of " + bev + ".")