
# 桁dp
# TLEなる....
import sys
sys.setrecursionlimit(10**7)

d, n = int(input()), input()
MOD = 10**9+7
memo = [[[None for _ in range(d + 1)] for _ in range(2)]
        for _ in range(len(n) + 1)]



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
        ret %= MOD
    memo[i][threshold][s%d] = ret
    return ret


print(rec(0, 1, 0) - 1)
