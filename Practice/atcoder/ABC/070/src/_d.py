# disjoint setかと思いきやDFS
# どこが悪いのかさっっっっっっぱりわからん...
# あ 再帰にしてるからその上限か
# したらTLEになったので根本的にやり方が間違ってるということ


import sys

sys.setrecursionlimit(10000000)

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append([b, c])
    graph[b].append([a, c])

q, k = map(int, input().split())
k = k - 1
# kからスタートしてぜんぶたどる
ans_list = [0 for _ in range(n)]


def dfs(node, used, weight):
    for data in graph[node]:
        if data[0] not in used:
            next_used = used[:]
            next_used.append(data[0])
            dfs(data[0], next_used, weight + data[1])
    ans_list[node] = weight


dfs(k, [k], 0)

for _ in range(q):
    a, b = map(lambda x: int(x) - 1, input().split())
    print(ans_list[a] + ans_list[b])
