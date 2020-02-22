n, r = map(int, input().split())
if n < 10:
    k = 10 - n
    kk = 100 * k
    print(r + kk)
else:
    print(r)

