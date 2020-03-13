import sys
sys.setrecursionlimit(10**6)
w = int(input())
n, k = map(int, input().split())
dp = [[[0 for _ in range(w + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
ab = [list(map(int, input().split())) for _ in range(n)]


def rec(i, ki, wi):
    if dp[i][ki][wi] > 0:
        return dp[i][ki][wi]
    if i == n or ki == 0:
        dp[i][ki][wi] = 0
        return 0
    if wi + ab[i][0] <= w:
        dp[i][ki][wi] = max(rec(i + 1, ki, wi),
                            rec(i + 1, ki - 1, wi + ab[i][0]) + ab[i][1])
    else:
        dp[i][ki][wi] = rec(i + 1, ki, wi)
    return dp[i][ki][wi]


print(rec(0, k, 0))