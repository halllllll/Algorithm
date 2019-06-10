# DPっぽい dp[iターン目で][放てるpの残数] = 勝ち数 - 負け数 の最大値
# メモリ的にもオーダー的にもギリ？ N^2
# なんかDP使ったらダメ間に合わないな.....

s = input()
dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]


def rec(i, p, res):
    if dp[i][p] > 0:
        return dp[i][p]
    if i == len(s):
        dp[i][p] = res
        return res
    if p > 0:
        dp[i][p] = max(rec(i + 1, p - 1, res + 1 if s[i] == "g" else res), rec(
            i + 1, p + 1, res - 1 if s[i] == "p" else res))
    else:
        dp[i][p] = rec(i + 1, p + 1, res - 1 if s[i] == "p" else res)
    return dp[i][p]


print(rec(0, 0, 0))
