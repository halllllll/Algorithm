# dfsでみる どうせ小さいので都度配列を渡していい
# 隣接リストでもつことにする
# クラスで管理するのすらめんどくさいのでlistオブジェクトでいいや

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    s, t = map(int, input().split())
    graph[s - 1].append(t - 1)
    graph[t - 1].append(s - 1)

ans = 0

path = [0, [0]]
stack = [path]

while len(stack) > 0:
    cur = stack.pop()
    if len(cur[1]) == n:
        ans += 1
    else:
        for g in graph[cur[0]]:
            if g not in cur[1]:
                nex = cur[1][:]
                nex.append(g)
                stack.append([g, nex])

print(ans)
