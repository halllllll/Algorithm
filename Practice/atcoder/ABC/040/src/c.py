# DFSするわけですが無駄があるのでDPです
# dfs関数などは要らんことに気づく。配列だけでいい
# dp = [i本目までの最小値]

# 再帰上限RE避け
import sys
sys.setrecursionlimit(sys.getrecursionlimit())

N = int(input())
A = list(map(int, input().split()))

DP = [None for _ in range(N)]
DP[0], DP[1] = 0, abs(A[0] - A[1])
for i in range(2, N):
    # 一歩前からの差 vs 2歩前からの差
    DP[i] = min(DP[i - 1] + abs(A[i] - A[i - 1]),
                DP[i - 2] + abs(A[i] - A[i - 2]))

print(DP[N-1])
