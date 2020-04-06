# 解説読んだけど「DAG上でDPして最短経路の数を求める」がサラッと書かれていて意味不明
# とりあえずワ―シャルフロイドでaからの全点間最短距離を求めてみる

from sys import setrecursionlimit

setrecursionlimit(10**7)

n = int(input())
a, b = map(int, input().split())
m = int(input())

INF = 10**10
graph = [[] for _ in range(n)]  # 最後に総数を探索するための隣接リスト
table = [[INF] * n for _ in range(n)]  # ワ―シャルフロイド用のやつ
for i in range(n):
    table[i][i] = 0
for _ in range(m):
    x, y = map(int, input().split())
    table[x - 1][y - 1] = 1
    table[y - 1][x - 1] = 1
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)

for k in range(n):
    for i in range(n):
        if table[i][k] == INF:
            continue
        for j in range(n):
            if table[k][j] == INF:
                continue
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

dist = table[a - 1][b - 1]

# 探索フェーズ
# iに至るまでの最短距離でよくね？DP無限にわからん
# わからんから雑に書くしか無いね

dp = {}
passed = [False for _ in range(n)]
passed[a - 1] = True


def dfs(i, cur, passed):
    if (i, cur) in dp:
        return dp[(i, cur)]
    if cur > dist:
        return 0
    if i == b - 1 and cur == dist:
        return 1
    ret = 0
    for next_node in graph[i]:
        if passed[next_node] == False:
            passed[next_node] = True
            ret += dfs(next_node, cur + 1, passed)
            ret %= 10**9 + 7
            passed[next_node] = False
    dp[(i, cur)] = ret
    return ret


print(dfs(a - 1, 0, passed))
