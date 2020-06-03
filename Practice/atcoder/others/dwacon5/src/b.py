# N的に全探索できるのでそうする
from functools import reduce
n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = []

for i in range(n):
    for j in range(i, n+1):
        if i == j:
            continue
        res.append(sum(arr[i:j]))

res = list(set(res))
# ここからk個選ぶ


res = list(sorted(res, reverse=True))[:k]
ans = reduce(lambda x, y: x & y, res)
print(ans)
