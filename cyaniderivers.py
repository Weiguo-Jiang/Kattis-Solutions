import math

towers = [int(t) for t in input()]
curMin = 0
startIndex = 0
endIndex = 1
while endIndex < len(towers):
    if towers[endIndex] == 0:
        endIndex += 1
    else:
        curMin = max(curMin, math.ceil((endIndex - startIndex - 1) / 2))
        startIndex = endIndex
        endIndex += 1
print(curMin)