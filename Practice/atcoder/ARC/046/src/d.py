# dpぽい気がするのでそうする
# なぜかREなる....
# pythonだとrecursion limitがアレなのを忘れていた...
# なぜかTLEなる....
# 文字列の加算がTLEの原因っぽかった（まじかよ）

import sys

sys.setrecursionlimit(10 ** 8)


s = input()
dp = {}


def rec(i, cur_g, cur_p, g, p):
    if i in dp:
        return dp[i]
    if i == len(s):
        ret = p - g
        dp[i] = ret
        return ret
    if cur_g > cur_p:
        # パーを出せる（出さなくてもいい）
        if s[i] == "g":
            ret = max(
                rec(i + 1, cur_g, cur_p + 1, g, p + 1),
                rec(i + 1, cur_g + 1, cur_p, g, p),
            )
            dp[i] = ret
            return ret
        elif s[i] == "p":
            ret = max(
                rec(i + 1, cur_g, cur_p + 1, g, p),
                rec(i + 1, cur_g + 1, cur_p, g + 1, p),
            )
            dp[i] = ret
            return ret
    else:
        # 勝てるかどうかにかかわらずグーを出すしか無い
        if s[i] == "g":
            ret = rec(i + 1, cur_g + 1, cur_p, g, p)
            dp[i] = ret
            return ret
        elif s[i] == "p":
            ret = rec(i + 1, cur_g + 1, cur_p, g + 1, p)
            dp[i] = ret
            return ret


print(rec(0, 0, 0, 0, 0))
