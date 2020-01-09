# 木全体の根が決まっているのでふつうにbfsでいい気がするが...
# 毎回探索するんじゃなくて、各枝にポイントをつけておいて、探索するときに1回だけ渡して更新していく
# 考え方は累積和
# なんかafter_contestってテストケースでハネられるんだが。。。。。なんだこれ
# i<jのときiのほうが根に近い、というのを決め打ちしても通ってしまう防止らしい
# 回避するべく
# 両方のノードからエッジを貼り(graph[b].append(a))、
# 探索のときに訪問済みの場所は抜くことにした(if node not in used:)

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
points = [0 for _ in range(n)]

for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(q):
    p, x = map(int, input().split())
    points[p - 1] += x

path = [0]
used = set()
used.add(0)
while len(path) > 0:
    cur_node = path.pop()
    cur_point = points[cur_node]
    for node in graph[cur_node]:
        if node not in used:
            used.add(node)
            points[node] += cur_point
            path.append(node)
print(" ".join(list(map(str, points))))
