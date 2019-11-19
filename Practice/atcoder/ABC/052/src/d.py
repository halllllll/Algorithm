# 典型dp
n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    ans += min((arr[i] - arr[i - 1]) * a, b)

print(ans)
