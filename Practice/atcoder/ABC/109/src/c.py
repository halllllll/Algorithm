n, x = map(int, input().split())
a = list(map(int, input().split()))

a.append(x)
a = list(sorted(a))
difs = []
for i in range(n - 1):
    difs.append(a[i + 1] - a[i])

