# 典型dpぽい見た目をしている
# 手元の3.4.3環境ではふつうに通るんだけどatcoderに提出するとなぜか一つも通らずREになってしまう
# wandboxで出たエラー修正 (d->dp)

w = int(input())
n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

# dp = [[[0 for _ in range(w + 1)] for _ in range(k + 1)] for _ in range(n + 1)] # これだとMLEなる（内包表記って遅いしメモリ効率悪いん？）

dp = [[[0] * (w + 1) for _ in range(k + 1)] for _ in range(n + 1)]  # これならいける

# じゃこれならもっと早い？ -> そもそも通らん
# dp = [[[0] * (w + 1)] * (k + 1) for _ in range(n + 1)]

# for i in range(n):
#     for j in range(k + 1):
#         for ww in range(w + 1):
#             if ww >= wv[i][0] and j >= 1:
#                 dp[i + 1][j][ww] = max(dp[i][j][ww],
#                                        dp[i][j - 1][ww - wv[i][0]] + wv[i][1])
#             else:
#                 dp[i + 1][j][ww] = dp[i][j][ww]
# print(dp[n][k][w])


def rec(i, ki, wi):
    if dp[i][ki][wi] > 0:
        return dp[i][ki][wi]
    if i == n or ki == 0:
        return 0

    if wi + wv[i][0] <= w:
        dp[i][ki][wi] = max(rec(i + 1, ki, wi),
                            rec(i + 1, ki - 1, wi + wv[i][0]) + wv[i][1])
    else:
        dp[i][ki][wi] = rec(i + 1, ki, wi)
    return dp[i][ki][wi]


print(rec(0, k, 0))