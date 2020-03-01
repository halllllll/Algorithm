n, w = map(int, input().split())

dp = [[0 for _ in range(w + 1)] for _ in range(n)]

vs, ws = [], []
for _ in range(n):
    vv, wv = map(int, input().split())
    vs.append(vv)
    ws.append(wv)

for i in range(w + 1):
    dp[0][i] = 0

for i in range(n):
    for j in range(w + 1):
        if j < ws[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - ws[i]] + vs[i])

print(dp[n - 1][w])
