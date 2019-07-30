# +2019までを調べれば十分

l, r = map(int, input().split())
ans = 10**9

for i in range(l, min(r+1, l+2020)):
  for j in range(i,  min(r+1, l+2020)):
    if i < j:
      ans = min(ans, (i * j)%2019)

print(ans)