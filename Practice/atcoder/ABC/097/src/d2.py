# さっきWAして答えみて再度アタック
# （ちなみに問題自体憶えてないけど昔やったことあってそんときゃACしてたので退化してるね 向いてないね やめたほうがいいね）
n, m = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))
par = [i for i in range(n)]


def root(x):
    # while x != par[x]:
    #     par[x] = root(par[x])
    # return par[x]
    # なぜか上記の書き方が駄目だった
    if x == par[x]:
        return x
    y = root(par[x])
    par[x] = y
    return y


def union(a, b):
    if a > b:
        a, b = b, a
    ra, rb = root(a), root(b)
    if ra != rb:
        par[ra] = rb


for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    union(x, y)

ans = 0
for i in range(n):
    ra, rb = root(i), root(p[i])
    if ra == rb:
        ans += 1
print(ans)
