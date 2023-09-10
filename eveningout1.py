A, B = map(int, input().split())

mod = A%B

print(min(mod, B-mod))