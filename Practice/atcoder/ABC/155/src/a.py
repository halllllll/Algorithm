d = {}
n = int(input())
c = 0
for _ in range(n):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
    c = max(c, d[s])
lis = sorted(d.items(), key=lambda x: x[1], reverse=True)
ans = []
for a in lis:
    if a[1] == c:
        ans.append(a[0])
ans = sorted(ans)
for v in ans:
    print(v)

