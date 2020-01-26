# 問題文がおかしい（「荷物の少なくとも1つの面が、ダンボールか他の荷物のある面にぴったりとくっつくように梱包します。」って「1 つのダンボールに自分の荷物を 1 つだけ梱包します」と矛盾しとるやんけ）
# 解法はわからんけどサンプルケースから無理やり生やすと、横でソートして縦でmax
from functools import reduce

c = int(input())
table = []
for _ in range(c):
    table.append(sorted(list(map(int, input().split()))))
ans = [0, 0, 0]
for i in range(3):
    for j in range(c):
        ans[i] = max(ans[i], table[j][i])
print(reduce(lambda x, y: x * y, ans))
