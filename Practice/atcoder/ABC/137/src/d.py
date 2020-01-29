# 優先度つきキューをやるらしい
# どうすんのと思ったら毎回条件があうまで探索してpushしてpopすんのか

import heapq

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key=lambda x: x[0])

idx = 0
ans = 0
heap = []
heapq.heapify(heap)
for i in range(1, m + 1):
    # i...残り日数
    while idx < n and arr[idx][0] <= i:
        heapq.heappush(heap, -arr[idx][1])
        idx += 1
    # この時点でヒープで次に取り出す値には残り日数iの時点での最大値（つーか最小値）が入っている
    if heap:
        ans = ans - heapq.heappop(heap)

print(ans)
