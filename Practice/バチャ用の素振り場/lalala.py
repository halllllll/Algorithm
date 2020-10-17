# iya-  これは気づかんて
h, w = map(int, input().split())
c = []
for _ in range(10):
    c.append(list(map(int, input().split())))
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])
ans = 0
for _ in range(h):
    for v in list(map(int, input().split())):
        if v > 1:
            ans += c[v][1]
print(ans)
