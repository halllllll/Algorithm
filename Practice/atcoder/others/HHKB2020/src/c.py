n = int(input())
p = list(map(int, input().split()))
ngs = set()
a = 0
idx = 0
while idx < n:
    if a < p[idx]:
        print(a)
        ngs.add(p[idx])
        idx += 1
    else:
        ngs.add(p[idx])
        b = a
        while a in ngs:
            a += 1
        ngs.add(b)
        c = idx
        while idx < n and p[c] >= p[idx]:
            idx += 1
            print(a)
