# 頭から倒せるだけ倒していく

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
  if a[i] <= b[i]:
    count += a[i]
    b[i] -= a[i]
    count += min(a[i+1], b[i])
    a[i+1] = max(0, a[i+1] - b[i])
  else:
    count += b[i]

print(count)