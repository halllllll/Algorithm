n = int(input())
INF = 10**16

# 隣接行列　初期化
graph = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
  graph[i][i] = 0

# 行列を埋めていく
for _ in range(n):
  line = list(map(int, input().split()))
  s, k = line[0], line[1]
  for t in range(k):
    graph[s][line[(t+1)*2]] = line[(t+1)*2+1]

visited = [False for _ in range(n)]
costs = [INF for _ in range(n)]

# 0をスタートにする
costs[0] = 0

while True:
  mincost = INF
  target_node = -1
  for i in range(n):
    if visited[i] == False and mincost > costs[i]:
      mincost = costs[i]
      target_node = i
  if target_node == -1:
    break
  
  visited[target_node] = True

  for i in range(n):
    if visited[i] == False and graph[target_node][i] == INF:
      continue
    # 更新するのは、target_nodeから伸ばしたときにそれまでのiに至るコストよりも小さくなる場合
    if graph[target_node][i] + costs[target_node] < costs[i]:
      costs[i] = graph[target_node][i] + costs[target_node]

for i in range(n):
  print("{} {}".format(i, costs[i]))