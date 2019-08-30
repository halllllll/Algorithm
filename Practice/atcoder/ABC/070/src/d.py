# KからDFS -> xからKまでとyからKまで

import sys
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[] for _ in range(n)]
costs = [0 for _ in range(n)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b-1, c))
    graph[b - 1].append((a-1, c))

q, k = map(int, input().split())


def dfs(cur, cost, p):
    for g in graph[cur]:
        if g[0] != p and costs[g[0]] == 0:
            costs[g[0]] = g[1] + cost
            dfs(g[0], costs[g[0]], cur)


dfs(k - 1, 0, -1)

for _ in range(q):
    x, y = map(int, input().split())
    print(costs[x-1]+costs[y-1])
