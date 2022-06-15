t = int(input())
for i in range(t):
	d, M = input().split()
	d = int(d)

	if (M == 'Mar' and d in range(21, 32)) or (M == 'Apr' and d in range(1, 21)):
		print("Aries")
	elif (M == 'Apr' and d in range(21, 32)) or (M == 'May' and d in range(1, 21)):
		print("Taurus")
	elif (M == 'May' and d in range(21, 32)) or (M == 'Jun' and d in range(1, 22)):
		print("Gemini")
	elif (M == 'Jun' and d in range(22, 32)) or (M == 'Jul' and d in range(1, 23)):
		print("Cancer")
	elif (M == 'Jul' and d in range(23, 32)) or (M == 'Aug' and d in range(1, 23)):
		print("Leo")
	elif (M == 'Aug' and d in range(23, 32)) or (M == 'Sep' and d in range(1, 22)):
		print("Virgo")
	elif (M == 'Sep' and d in range(22, 32)) or (M == 'Oct' and d in range(1, 23)):
		print("Libra")
	elif (M == 'Oct' and d in range(23, 32)) or (M == 'Nov' and d in range(1, 23)):
		print("Scorpio")
	elif (M == 'Nov' and d in range(23, 32)) or (M == 'Dec' and d in range(1, 22)):
		print("Sagittarius")
	elif (M == 'Dec' and d in range(22, 32)) or (M == 'Jan' and d in range(1, 21)):
		print("Capricorn")
	elif (M == 'Jan' and d in range(21, 32)) or (M == 'Feb' and d in range(1, 20)):
		print("Aquarius")
	else:
		print("Pisces")