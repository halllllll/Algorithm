n, x, t = map(int, input().split())
now = 0
while n > 0:
    now += t
    n -= x
print(now)