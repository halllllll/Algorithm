# disjoint setかと思いきやDFS
# したらTLEになったので根本的にやり方が間違ってるということ
# よくよく考えたらdfsなのでそこにたどり着いたときが最短距離だわ ムダに探索してた
# Pypyだと残り1TLE, Pythonだとちょっときついけど間に合う感じになった。。

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


def dfs(node, weight):
    for data in graph[node]:
        if not used[data[0]]:
            used[data[0]] = True
            dfs(data[0], weight + data[1])
    ans_list[node] = weight


used = [False for _ in range(n)]
used[k] = True
dfs(k, 0)

for _ in range(q):
    a, b = map(lambda x: int(x) - 1, input().split())
    print(ans_list[a] + ans_list[b])
