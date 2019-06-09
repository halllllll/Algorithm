# 一次元DPをMに踏まないように更新 踏まないようにっつーか踏んだらリセット

n, m = map(int, input().split())

ngs = [True for _ in range(n+1)]
for _ in range(m):
    ngs[int(input())] = False
dp = [0 for _ in range(n+1)]

dp[0] = 1
# 一段目確定
if ngs[1]:
    # 一通りだけ
    dp[1] = 1

for i in range(2, n+1):
    if ngs[i] == False:
        # たどりついてはいけない
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n] % 1000000007)
