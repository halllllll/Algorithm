# 数の少ないものから消すと考える
n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
for a in arr:
  if a not in d:
    d[a] = 1
  else:
    d[a] += 1

t = len(d)

d = list(sorted(d.items(), key = lambda x : x[1]))
if t <= k:
  print(0)
else:
  count = 0
  for di in d[:t-k]:
    count += di[1]
  print(count)