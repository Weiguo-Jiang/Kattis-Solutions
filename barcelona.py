n, k = map(int, input().split())
l = list(map(int, input().split()))
if l[0] == k:
    print("fyrst")
elif l[1] == k:
    print("naestfyrst")
else:
    for i in range(2, len(l)):
        if l[i] == k:
            print(str(i+1) + " fyrst")