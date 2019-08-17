v, e = map(int, input().split())
INF = 10**16
g = [[INF for _ in range(v)] for _ in range(v)]
for _ in range(e):
  s, t, d = map(int, input().split())
  g[s][t] = d


# 自分へのループ
for i in range(v):
    g[i][i] = 0


for k in range(v):
  for i in range(v):
    if g[i][k] == INF:
      continue
    for j in range(v):
      if g[k][j] == INF:
        continue
      g[i][j] = min(g[i][j], g[i][k]+g[k][j])

# 負の閉路ができてしまっているか確認
for i in range(v):
  if g[i][i]<0:
    print("NEGATIVE CYCLE")
    exit()

for i in range(v):
  ans = []
  for j in range(v):
    if g[i][j] == INF:
      ans.append("INF")
    else:
      ans.append(str(g[i][j]))
  print(" ".join(ans))
