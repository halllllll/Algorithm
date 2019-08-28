# ただの典型いもす

n, m = map(int, input().split())
arr = [0 for _ in range(n+1)]
for _ in range(m):
    l, r = map(int, input().split())
    arr[l - 1] += 1
    arr[r] -= 1

for i in range(1, n):
    arr[i] += arr[i - 1]

count = 0
for i in range(n):
    if arr[i] == m:
        count += 1

print(count)
