# なぜかrubyでREになるので仕方なくpythonで
# 桁dp
# ??????????????なんか同じ場所でREなる............................

d, n = int(input()), input()

memo = [[[None for _ in range(d + 1)] for _ in range(2)]
        for _ in range(len(n)+1)]


def rec(i, threshold, s):
    if i == len(n):
        return 1 if s == 0 else 0

    if memo[i][threshold][s] is not None:
        return memo[i][threshold][s]

    ret = 0
    limit = int(n[i]) if threshold == 1 else 9
    for j in range(limit + 1):
        nex_threshold = 1 if (j == limit and threshold == 1) else 0
        ret += rec(i + 1, nex_threshold, (s + j) % d)
        ret %= 10 ** 9 + 7
        memo[i][threshold][s] = ret

    return ret


print(rec(0, 1, 0) - 1)
