# 累積和をととっといて比較
n = int(input())
arr = list(map(int, input().split()))

ruiseki = [0 for _ in range(n)]
ruiseki[0] = arr[0]

for i in range(1, n):
    ruiseki[i] += ruiseki[i - 1] + arr[i]

inf = 10 ** 20
ans = inf

for i in range(n - 1):
    x = ruiseki[i]
    y = ruiseki[-1] - x
    ans = min(ans, abs(x - y))
print(ans)
