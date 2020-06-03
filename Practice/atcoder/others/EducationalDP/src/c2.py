# dp[i日目][i-1日目にどれを選んだか] = i日目までの最大の幸福度
# これはメモ化再帰でやってみたバージョン

import sys

sys.setrecursionlimit(10 ** 8)

n = int(input())
a, b, c = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

dp = [[-1 for _ in range(3)] for _ in range(n + 1)]
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]


def rec(i, choice):
    if dp[i][choice] >= 0:
        return dp[i][choice]
    if i == n:
        return 0
    ret = 0  # ループじゃなくてifでやってるのでそれぞれ確実に大きい値が入る（ので更新する必要がない）
    if choice == 0:
        ret = a[i] + max(rec(i + 1, 1), rec(i + 1, 2))
    elif choice == 1:
        ret = b[i] + max(rec(i + 1, 0), rec(i + 1, 2))
    elif choice == 2:
        ret = c[i] + max(rec(i + 1, 0), rec(i + 1, 1))
    dp[i][choice] = ret
    return ret


print(max(rec(0, 0), rec(0, 1), rec(0, 2)))
