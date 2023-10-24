r, f = map(int, input().split())
rate = 180/r
rotation = rate*f%360
if 0 <= rotation < 90 or 270 < rotation <= 360:
    print("up")
else:
    print("down")