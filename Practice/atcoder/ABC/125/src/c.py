# できるだけ正数が多いほうが良い。隣り合う負数は正にできる
# あと-+++++は+++++-のように-を移動できるので隣り合わせられる
# -が奇数なら0以上の最小の数に-を割り当ててあとは合計
# 偶数ならすべての-を+にできる

from functools import reduce

n = int(input())
minn = 10**9
arr = list(map(int, input().split()))
minus = 0
ans = reduce(lambda x, y: abs(x) + abs(y), arr)
for i in range(n):
    if arr[i] < 0:
        minus += 1
    if minn > abs(arr[i]):
        minn = abs(arr[i])
if minus % 2 == 0:
    print(ans)
else:
    print(ans-minn*2)
