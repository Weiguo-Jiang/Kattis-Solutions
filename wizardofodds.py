from math import log2
N, K = list(map(int, input().split()))
if K >= log2(N):
	print("Your wish is granted!")
else:
	print("You will become a flying monkey!")