# DFS典型でいいのでは
# すべての場所から探索すると爆発しそう、なのでスタートする箇所の候補を最初にピックする
# 最長経路があるとすればできるだけその経路のはじっこをスタートにするのがよさそう
# ....とか考えたけど愚考であった（答え見た）
# 各マスをスタートとしたとき、最大でどこまで伸ばせるかを全探索する

n, m = int(input()), int(input())
table = []
for _ in range(m):
    table.append(list(map(int, input().split())))
ans = 0


def dfs(t, y, x, d):
    global ans
    steps = [0, 1, 0, -1, 0]
    t[y][x] = 0
    simensoka = True
    for i in range(4):
        ny, nx = y + steps[i], x + steps[i + 1]
        if 0 <= ny < m and 0 <= nx < n:
            if t[ny][nx] == 1:
                simensoka = False
                dfs(t, ny, nx, d + 1)
    t[y][x] = 1
    if simensoka:
        ans = max(ans, d + 1)


for i in range(m):
    for j in range(n):
        if table[i][j] == 1:
            dfs(table, i, j, 0)

print(ans)