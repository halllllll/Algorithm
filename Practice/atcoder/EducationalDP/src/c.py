# dp[i日目][i-1日目にどれを選んだか] = i日目までの最大の幸福度
# これはループでやってみたバージョン

n = int(input())
a, b, c = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

dp = [[-1 for _ in range(3)] for _ in range(n + 1)]
# 初期値、最初間違えて0にしてた
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]
for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = a[i] + max(dp[i - 1][1], dp[i - 1][2])
        elif j == 1:
            dp[i][j] = b[i] + max(dp[i - 1][0], dp[i - 1][2])
        elif j == 2:
            dp[i][j] = c[i] + max(dp[i - 1][1], dp[i - 1][0])
print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
