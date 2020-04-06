# 日本語が難しいワ―シャルフロイド
n, m = map(int, input().split())
INF = 10**10
table = [[INF] * n for _ in range(n)]
for i in range(n):
    table[i][i] = 0
for _ in range(m):
    a, b, t = map(int, input().split())
    table[a - 1][b - 1] = t
    table[b - 1][a - 1] = t

for k in range(n):
    for i in range(n):
        if table[i][k] == INF:
            continue
        for j in range(n):
            if table[k][j] == INF:
                continue
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

ans = 10**10
for i in range(n):
    tmp = 0
    for j in range(n):
        if i == j:
            continue
        tmp = max(tmp, table[i][j])
    if tmp > 0:
        ans = min(ans, tmp)
print(ans)