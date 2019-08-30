# 奇数の数が奇数個ならあまる（偶数はいくつあっても最終的に1つの偶数にできるので関係ない）

n = int(input())
arr = list(map(int, input().split()))

odd_count = len(list(filter(lambda x : x%2==1, arr)))
if odd_count%2==1:
  print("NO")
else:
  print("YES")