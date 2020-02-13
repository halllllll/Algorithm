# 桁DP練習しにきた
import sys

sys.setrecursionlimit(10 ** 8)
a, b = input().split()
# まずbまでに含まれるのを求め、次にa-1までに含まれるのを求めると、包摂原理によりその差が答えになる
# うーんこのやり方だと毎回tableをもたせないといけないのか？？？？毎回それぞれ計算が必要になるじゃん


def rec(i, smaller, include4or9, s, table):
    if (i, smaller, include4or9) in table:
        return table[(i, smaller, include4or9)]
    if i == len(s):
        table[(i, smaller, include4or9)] = 1 if include4or9 else 0
        return table[(i, smaller, include4or9)]
    ret = 0
    upper = 10 if smaller else int(s[i]) + 1
    for j in range(upper):
        ret += rec(
            i + 1,
            True if smaller or j < int(s[i]) else False,
            True if include4or9 or j == 4 or j == 9 else False,
            s,
            table,
        )
    table[(i, smaller, include4or9)] = ret
    return table[(i, smaller, include4or9)]


ans_b, ans_a = rec(0, False, False, b, {}), rec(0, False, False, str(int(a) - 1), {})
print(ans_b - ans_a)
