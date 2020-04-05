# 同じ木に属する(==そこまでたどりつけるかどうか）の判定にunionfind
# 同じ木に属しているノードはあとで数えることができる（そうだね）
# 除外するやつが出てくる。直の友達+ブロック関係にあるやつ（と自分）
# 同じ木に属しているノードの総数 - (直の友達+ブロック関係+自分自身)が答え
from sys import setrecursionlimit
setrecursionlimit(10**8)
n, m, k = map(int, input().split())
par = [i for i in range(n)]
ans = [0 for _ in range(n)]


def root(x):
    if x == par[x]:
        return x
    y = root(par[x])
    par[x] = y
    return y


def union(x, y):
    if x > y:
        x, y = y, x
    rx, ry = root(x), root(y)
    if rx != ry:
        par[ry] = rx


friends = [[] for _ in range(n)]
blocks = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)
for _ in range(k):
    c, d = map(int, input().split())
    blocks[c - 1].append(d - 1)
    blocks[d - 1].append(c - 1)

# 木に属しているやつを数えるぜ
group_count = [0 for _ in range(n)]
for i in range(n):
    group_count[root(i)] += 1
# 答えを作るぜ
for i in range(n):
    # 初期化（じゃないけど）
    ans[i] += group_count[root(i)]
    # 直の友達を除く
    ans[i] -= len(friends[i])
    # ブロックしてるやつを除く
    for b in blocks[i]:
        ra, rb = root(i), root(b)
        if ra == rb:
            ans[i] -= 1
    # 自分自身を除く
    ans[i] -= 1
print(" ".join(list(map(str, ans))))
