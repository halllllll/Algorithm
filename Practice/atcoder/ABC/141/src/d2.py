# 「毎回最大のやつ取れない限り無理じゃね...?」 <- それできます。優先度付きキューならね
import heapq
from functools import reduce
n, m = map(int, input().split())
arr = list(map(lambda x: int(x) * -1, input().split()))
heapq.heapify(arr)
for i in range(m):
    t = -1 * heapq.heappop(arr)
    heapq.heappush(arr, -1 * (t // 2))
print(-1 * reduce(lambda a, b: a + b, arr))
