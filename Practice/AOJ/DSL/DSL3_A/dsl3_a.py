# 尺取を使う その1
n, s = map(int, input().split())
arr = list(map(int, input().split()))
INF = 2 ** 31 - 1
ans = INF
tmp = 0
r = 0
for l in range(n):
    while r < n and tmp < s:
        tmp += arr[r]
        r += 1

    if tmp >= s:
        ans = min(ans, r - l)
    if r == l:
        r += 1
    else:
        tmp -= arr[l]

print(0 if ans == INF else ans)
