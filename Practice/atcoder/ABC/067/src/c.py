# 累積和が見える
n = int(input())
a = list(map(int, input().split()))
ruiseki = [0 for _ in range(n)]
ruiseki[0] = a[0]
for i in range(1, n):
    ruiseki[i] = ruiseki[i - 1] + a[i]

ans = 10 ** 16
for i in range(n - 1):
    ans = min(ans, abs(ruiseki[-1] - ruiseki[i] * 2))

print(ans)
