# DPなのはわかるとして構築がまったくできん、手続き的に書いたやつをforで書き換えただけ

n = int(input())
arr = list(map(int, input().split()))
if n == 2:
    print(abs(arr[0] - arr[1]))
    exit()
dp = [10 ** 9 for _ in range(n)]
dp[0] = abs(arr[0] - arr[1])
dp[1] = min(abs(arr[2] - arr[0]), abs(arr[2] - arr[1]) + dp[0])

for i in range(3, n):
    dp[i - 1] = min(
        abs(arr[i] - arr[i - 1]) + dp[i - 2], abs(arr[i] - arr[i - 2]) + dp[i - 3]
    )

# dp[2] = min(abs(arr[3] - arr[2]) + dp[1], abs(arr[3] - arr[1]) + dp[0])
# dp[3] = min(abs(arr[4] - arr[3]) + dp[2], abs(arr[4] - arr[2]) + dp[1])
# dp[4] = min(abs(arr[5] - arr[4]) + dp[3], abs(arr[5] - arr[3]) + dp[2])

print(dp[-2])
