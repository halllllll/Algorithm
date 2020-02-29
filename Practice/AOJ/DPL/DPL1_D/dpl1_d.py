# O(NlogN)でできる最長増加部分列があるときいて
# にぶたんを使う
from bisect import bisect_left

n = int(input())
arr = [int(input()) for _ in range(n)]
INF = 10 ** 16

dp = [INF for _ in range(n + 1)]

# まずふつうのO(N^2)のやつ
# これだとTLEなった
# ans = 0
# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j]+1)
#         ans = max(ans, dp[i])

# print(ans)
dp[0] = -1
for i in range(n):
    idx = bisect_left(dp, arr[i])
    dp[idx] = arr[i]

idx = bisect_left(dp, INF) - 1
print(idx)
