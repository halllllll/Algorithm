# 全探索の気持ちが芽生える なにを全探索する？
# Qだと2^50なので無理になる、
# Nをしたいが10^10では？と無理になる
# と思いきや条件からA[i-1]<=A[i]なのでだいぶ減りそうとなる
# 計算量の見積もりがぜんぜんできないがたぶんいけるとなる
from collections import deque
n, m, q = map(int, input().split())
queries = []
for _ in range(q):
    queries.append(tuple(map(int, input().split())))

queue = deque()
for i in range(1, m + 1):
    queue.append([i])

ans = 0


def calc(arr):
    ret = 0
    for a, b, c, d in queries:
        if arr[b - 1] - arr[a - 1] == c:
            ret += d
    return ret


while len(queue):
    nex_queue = deque()
    for qq in queue:
        if len(qq) == n:
            ans = max(ans, calc(qq))
        else:
            for i in range(qq[-1], m + 1):
                nex_qq = qq[:]
                nex_qq.append(i)
                nex_queue.append(nex_qq)
    queue = nex_queue

print(ans)