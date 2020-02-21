# 桁DPの練習にきました
n = input()

dp = {}


def rec(i, smaller, cur):
    if (i, smaller, cur) in dp:
        return dp[(i, smaller, cur)]
    if i == len(n):
        dp[(i, smaller, cur)] = cur
        return cur
    upper = 10 if smaller else int(n[i]) + 1
    ret = 0
    for j in range(upper):
        ret += rec(
            i + 1,
            True if smaller or j < int(n[i]) else False,
            cur + 1 if j == 1 else cur,
        )
    dp[(i, smaller, cur)] = ret
    return ret


print(rec(0, False, 0))
