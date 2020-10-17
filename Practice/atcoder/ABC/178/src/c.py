import sys
sys.setrecursionlimit(10**9)

n = int(input())
mod = 10**9 + 7

# 再帰だとなんか通らん
# dp = {}
# def rec(i, zero, nine):
#     if (i, zero, nine) in dp:
#         return dp[(i, zero, nine)]
#     if i == n:
#         return 1 if (zero and nine) else 0
#     ret = 0
#     for j in range(10):
#         if j == 0:
#             ret += rec(i + 1, True, nine)
#         elif j == 9:
#             ret += rec(i + 1, zero, True)
#         else:
#             ret += rec(i + 1, zero, nine)
#         ret %= mod
#     dp[(i, zero, nine)] = ret
#     return ret

# print(rec(0, False, False))

dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(10**6 + 100)]
dp[0][0][0] = 1  # どういう意味なのかは不明
for i in range(n):
    for j in range(2):
        for k in range(2):
            for m in range(10):
                if m == 0:
                    dp[i + 1][1][k] += dp[i][j][k]
                    dp[i + 1][1][k] %= mod
                elif m == 9:
                    dp[i + 1][j][1] += dp[i][j][k]
                    dp[i + 1][j][1] %= mod
                else:
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j][k] %= mod
print(dp[n][1][1])
# 869121

# 2511445
