n, m = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
for a in arr:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
dd = [[k, v] for k, v in d.items()]
dd = sorted(dd, key=lambda x: x[1])
if dd[-1][1] > n // 2:
    print(dd[-1][0])
else:
    print("?")
