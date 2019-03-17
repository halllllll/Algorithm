# よくわからんが隣接リストのDFSで間に合うのでは

# 酔ってるせいのはずだが実装が合わない kuso

# 消したら困るのでとりあえずgit commitしとくわ ザマミロ俺
n, m = map(int, input().split())
gets = []
for _ in range(m):
    s, t = map(int, input().split())
    gets.append([s-1, t-1])
ans = 0
for i in range(m):
    graph = [[] for _ in range(n)]
    dis_idx = 0
    for j in range(m):
        if i == j:
            continue
        else:
            s, t = gets[j]
            graph[s].append(t)
            graph[t].append(s)

    # 連結木になるか探索
    stack = []
    for g in graph:
        if len(g) != 0:
            stack = g
            break
    print("start by ", stack)
    visited = [False for _ in range(len(graph))]
    while len(stack) > 0:
        nex = stack.pop()
        for ni in graph[nex]:
            if visited[ni] == False:
                visited[ni] = True
                stack.append(ni)
    # 判定 すべてのノードを通ったかどうか
    count = list(filter(lambda x: x == True, visited))
    if len(count) != n:
        print("fuck in ", i)
        for g in graph:
            print(g)
    ans += 1 if len(count) == n else 0
print(n-ans)
