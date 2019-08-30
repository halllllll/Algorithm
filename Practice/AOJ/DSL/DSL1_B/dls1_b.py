import sys
sys.setrecursionlimit(10**9)
"""
重み付きで経路圧縮
ランクでの比較は考えず、圧縮だけする
"""


class WeightedUnionFindTree:
    def __init__(self, n):
        self.par = list(range(n))
        self.weight = [0 for _ in range(n)]

    def root(self, t):
        if t == self.par[t]:
            return t
        # 経路圧縮してみる
        r = self.root(self.par[t])
        self.weight[t] += self.weight[self.par[t]]
        self.par[t] = r
        return r

    def rec_weight(self, t):
        if t == self.par[t]:
            return 0
        return self.weight[t] + self.rec_weight(self.par[t])

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y, w):
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx != rooty:
            if y != rooty:
                # 直接yにつなげる
                self.weight[rootx] = w - self.rec_weight(x)
            else:
                # 根につなげる
                self.weight[rootx] = w - (self.weight[x] - self.weight[y])
            self.par[rootx] = y

    def diff(self, x, y):
        if self.same(x, y):
            # xからxの根への重さ - (yからyの根への重さ)
            return self.rec_weight(x) - self.rec_weight(y)
        else:
            return "?"


n, q = list(map(int, input().split()))
wuft = WeightedUnionFindTree(n)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        x, y, w = query[1], query[2], query[3]
        wuft.unite(x, y, w)
    elif query[0] == 1:
        x, y = query[1], query[2]
        print(wuft.diff(x, y))
