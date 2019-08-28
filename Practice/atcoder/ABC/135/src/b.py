n = int(input())
arr = list(map(int, input().split()))
sorted_arr = list(sorted(arr))
count = 0
for i in range(n):
  if arr[i] != sorted_arr[i]:
    count += 1

if count <= 2:
  print("YES")
else:
  print("NO")
