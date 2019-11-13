import sys

sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
par = list(range(0, n))


def root(x):
    if x == par[x]:
        return x
    else:
        r = root(par[x])
        par[x] = r
        return r


def same(x, y):
    return root(x) == root(y)


def union(x, y):
    if not same(x, y):
        # not `par[x] = y`
        par[root(x)] = y


for _ in range(m):
    q, x, y = map(int, input().split())
    if q == 0:
        union(x, y)
    else:
        print("1" if same(x, y) else "0")
