# ワーシャルフロイドで解くバージョン
h, w = map(int, input().split())
INF = 10 ** 10
table = [[INF] * 10 for _ in range(10)]

for i in range(10):
    column = list(map(int, input().split()))
    for j in range(10):
        if i == j:
            continue
        table[i][j] = column[j]

wall = {}
for _ in range(h):
    for a in list(map(int, input().split())):
        if a not in wall:
            wall[a] = 1
        else:
            wall[a] += 1

for k in range(10):
    for i in range(10):
        for j in range(10):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

ans = 0
for k, v in wall.items():
    if k != -1 and k != 1:
        ans += table[k][1] * v
print(ans)
