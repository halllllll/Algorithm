# 尺取
n, k = map(int, input().split())
arr = list(map(int, input().split()))

r = 0
s = 0
count = 0
for l in range(n):
    while r < n and s < k:
        s += arr[r]
        r += 1

    if n == r:
        # あとは減る一方
        while s >= k and l <= n:
            s -= arr[l]
            count += 1
            l += 1
        break
    else:
        count += n + 1 - r
        s -= arr[l]
        l += 1
print(count)
