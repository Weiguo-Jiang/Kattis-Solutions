ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

ds = -1*ds
dm = -1*dm

while True:
    if ds == dm:
        print(ds)
        break
    elif ds > dm:
        dm += ym
    else:
        ds += ys