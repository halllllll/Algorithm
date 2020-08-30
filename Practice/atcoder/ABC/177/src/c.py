n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
ans = 0
s = sum(a) - a[0]
for i in range(1, n):
    ans += a[i - 1] * s
    ans %= mod
    s -= a[i]
print(ans - s)
