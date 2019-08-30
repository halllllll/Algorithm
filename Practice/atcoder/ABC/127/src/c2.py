# 解き直し

n, m = map(int, input().split())

arr = [0 for _ in range(n+2)]
for _ in range(m):
  l, r = map(int, input().split())
  arr[l] += 1
  arr[r+1] -= 1

for i in range(n):
  arr[i+1] += arr[i]

count = 0
for ai in arr:
  if ai == m:
    count += 1

print(count)