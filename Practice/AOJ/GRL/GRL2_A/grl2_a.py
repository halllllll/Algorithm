# クエリを与えられるタイプのクラスカル
# クラスカル自体はAlDS1_12Aでやったのでほとんど流用するだけ

n, m = map(int, input().split())
graph = []


class Edge:
  def __init__(self, u, v, cost):
    self.u = u
    self.v = v
    self.cost = cost


parent = [i for i in range(n)]


def root(x):
  if x == parent[x]:
    return x
  else:
    parent[x] = root(parent[x])
    return parent[x]


# 最小のコスト順からやるっていうからには
# いったんすべてを取らねばならない....
for _ in range(m):
  u, v, cost = map(int, input().split())
  e = Edge(u, v, cost)
  graph.append(e)

graph = sorted(graph, key=lambda g: g.cost)

# そんで探索
ans = 0
for e in graph:
  u, v = root(e.u), root(e.v)
  if u != v:
    parent[v] = u
    ans += e.cost

print(ans)
