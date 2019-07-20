
l, r = map(int, input().split())
ans = 10 ** 9
for i in range(l, r + 1):
  for j in range(l, r + 1):
    if i == j:
      continue
    ans = min(ans, (i * j) % 2019)
    if ans == 0:
      print(ans)
      exit()

print(ans)