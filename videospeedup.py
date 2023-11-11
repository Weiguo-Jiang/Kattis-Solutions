n, p, k = map(int, input().split())
timestamps = [0] + list(map(int, input().split())) + [k]
multiplier = 1

time = 0
for i in range(len(timestamps)-1):
    time += (timestamps[i+1]-timestamps[i])*multiplier
    multiplier += p/100
print(time)