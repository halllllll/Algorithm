# 毎回ソートしても別にいいんじゃないの -> ダメでした
# 毎回最大のものがほしいならheapq使うか
import heapq

n, m = map(int, input().split())
# heapは最小のものを取り出すので予め-1をかけて大小を見かけ上逆転しておく
arr = list(map(lambda x: int(x) * -1, input().split()))
heapq.heapify(arr)
for _ in range(m):
    a = heapq.heappop(arr)
    # 負数にしたときの誤差がめんどくさい
    a *= -1
    a //= 2
    heapq.heappush(arr, a * -1)
print(sum(arr) * -1)
