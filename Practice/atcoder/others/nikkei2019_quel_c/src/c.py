n = int(input())
a, b, c = [], [], []
for i in range(n):
    av, bv = map(int, input().split())
    a.append(av)
    b.append(bv)
    c.append((i, av + bv))

c = sorted(c, key=lambda x: x[1], reverse=True)
takahaship, aokip = 0, 0
i = 0
for _ in c:
    if i % 2 == 0:
        takahaship += a[c[i][0]]
    else:
        aokip += b[c[i][0]]
    i += 1
print(takahaship - aokip)
