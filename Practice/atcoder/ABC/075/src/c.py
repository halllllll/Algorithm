# よくわからんが隣接リストのDFSで間に合うのでは

n, m = map(int, input().split())
gets = []  # とっておく
for _ in range(m):
    s, t = map(int, input().split())
    gets.append([s-1, t-1])
ans = 0
for i in range(m):
    graph = [[] for _ in range(n)]  # 隣接リスト
    for j in range(m):
        # 採用しない橋以外を採用する
        if i != j:
            s, t = gets[j]
            graph[s].append(t)
            graph[t].append(s)
    stack = [0]
    visited = [False for _ in range(n)]
    # 適当に0から始めて伸ばす
    visited[0] = True
    while len(stack):
        nex = stack.pop()
        for g in graph[nex]:
            if visited[g] == False:
                visited[g] = True
                stack.append(g)
    count = list(filter(lambda x: x == True, visited))
    ans += 1 if n-len(count) > 0 else 0

print(ans)
