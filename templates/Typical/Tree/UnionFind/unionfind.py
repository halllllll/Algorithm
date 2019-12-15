# 高さのなんかあのアレ（名前失念）はしない
# 思い出した ランク付け

import sys
sys.setrecursionlimit(1000000)

n, q = map(int, input().split())
Graph = [i for i in range(n)]


def find(x):
    if Graph[x] != x:
        Graph[x] = find(Graph[x])
    return Graph[x]


def unite(x, y, w):
    x_parent, y_parent = find(x), find(y)
    if x_parent != y_parent:
        Graph[x_parent] = y_parent


def same(x, y):
    x_parent, y_parent = find(x), find(y)
    if x_parent != y_parent:
        return False
    else:
        return True


for _ in range(q):
    query, l, r = map(int, input().split())
    if query == 0:
        unite(l, r)
    else:
        if same(l, r):
            print(1)
        else:
            print(0)
