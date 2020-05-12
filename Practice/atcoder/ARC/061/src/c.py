n, k = map(int, input().split())
d = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a in d:
        d[a] += b
    else:
        d[a] = b
dd = [(k, v) for k, v in d.items()]
dd = sorted(dd, key=lambda x: x[0])
cur = 0
tmp = -1
for a, b in dd:
    if cur >= k:
        break
    cur += b
    tmp = a
print(tmp)