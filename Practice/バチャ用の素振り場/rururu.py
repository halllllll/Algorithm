# いらない辺の数を求める かわいそう
# あらかじめ全点間での最小コストを求めておいて、
# M個目の辺bが存在しないとしたときのiからjへの最短経路を求め、
# それが最初に求めた最小パスと同じならば、
# 辺bはiからjへの最短経路を構築するのに必要であったといえそう
# 逆にいえば、最小パスと異なっていればいらない辺 ばいばい

n, m = map(int, input().split())
INF = 10**18
g = [[INF] * n for _ in range(n)]
bridges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a - 1][b - 1] = c
    g[b - 1][a - 1] = c
    bridges.append((a, b, c))

# あらかじめ求めておく全点間での最小コスト（ワーシャルフロイド
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

count = 0

for i in range(m):
    # i番目の辺はなかったことに
    g[bridges[i][0]][bridges[i][1]] = INF

    # jからi以外の各頂点への最短距離はBFSでいける？
    gg = [[INF] * n for _ in range(n)]
    for j in range(n):

        q = [j]

    # もとに戻す
    g[bridges[i][0]][bridges[i][1]] = bridges[i][2]

print(count)