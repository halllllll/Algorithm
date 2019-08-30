# primよりもクラスカル法のほうが楽らしい
# unionfindを使って追加する辺を判断
# 辺はソートして小さいやつからとっていく
# edgesをコストの昇順でやればwhileはしないでいける？


class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

    def __repr__(self):
        return repr((self.u, self.v, self.cost))


graph = []
n = int(input())
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] >= 0:
            e = Edge(i, j, line[j])
            graph.append(e)

graph = sorted(graph, key=lambda g: g.cost)
parent = [i for i in range(n)]


def root(x):
    if x == parent[x]:
        return parent[x]
    else:
        parent[x] = root(parent[x])
        return parent[x]


def unite(a, b):
    a = root(a)
    b = root(b)
    if a != b:
        parent[b] = a


ans = 0
for g in graph:
    u, v = root(g.u), root(g.v)
    if u != v:
        unite(u, v)
        ans += g.cost

print(ans)
