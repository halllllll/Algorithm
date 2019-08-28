n = int(input())
arr = list(map(int, input().split()))
maxn = 10e9
for i in range(1, n):
    sum1, sum2 = sum(arr[:i]), sum(arr[i:])
    maxn = min(maxn, abs(sum1 - sum2))

print(maxn)
