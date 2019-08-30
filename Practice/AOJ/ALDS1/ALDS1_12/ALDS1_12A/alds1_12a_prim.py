# あんまよく理解してない

n = int(input())
# 隣接行列
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

# MSTに追加されてるかどうか
visited = [False for _ in range(n)]
# iの親はparent[i]とする
parent = [-1 for _ in range(n)]
# 最終的にどんな意味があるのかよくわからんやつ
costs = [10 ** 10 for _ in range(n)]

costs[0] = 0

while True:
    target = 10 ** 10
    nex = -1
    # 次の点を確定させる
    for i in range(n):
        if visited[i] == False and costs[i] < target:
            nex = i
            target = costs[i]
    if nex == -1:
        break
    visited[nex] = True
    # 確定した点につながる辺のコストを最小のやつに更新
    # かつ、つながったら親も更新
    for i in range(n):
        if visited[i] or graph[nex][i] == -1:
            continue
        if graph[nex][i] < costs[i]:
            costs[i] = graph[nex][i]
            parent[i] = nex

# 計算 全域木なのでつながってないところは無視して残りの和を出す
ans = 0
for i in range(n):
    if parent[i] != -1:
        ans += graph[i][parent[i]]

print(ans)
