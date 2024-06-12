n = int(input())
dic = dict()
for _ in range(n):
    name, views = input().split()
    views = int(views)
    dic[name] = dic.get(name, 0) + views

print(max(dic, key=dic.get))
