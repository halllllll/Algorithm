# グラフわからんのでグラフアルゴリズム忘れた
# dfsでやる 限度2回c
# なんかしらんけどdfsが2TLEになるので諦めた それぞれの島について1とNがあれば良い

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for g in graph[1 : n - 1]:
    c = 0
    for v in g:
        if c >= 2:
            break
        if v == 0 or v == n - 1:
            c += 1
    if c == 2:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
