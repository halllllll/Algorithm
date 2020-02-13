# 桁DPの練習にきました

n = input()
k = int(input())

dp = {}


def rec(i, smaller, count):
    if (i, smaller, count) in dp:
        return dp[(i, smaller, count)]
    if i == len(n):
        dp[(i, smaller, count)] = 1 if count == k else 0
        return dp[(i, smaller, count)]
    ret = 0
    upper = 10 if smaller else int(n[i]) + 1
    for j in range(upper):
        ret += rec(
            i + 1,
            True if smaller or j < int(n[i]) else False,
            count + 1 if 0 < j else count,
        )
    dp[(i, smaller, count)] = ret
    return ret


print(rec(0, False, 0))
