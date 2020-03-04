# クラスカルとかワ―シャルフロイドなんかのグラフ探索だとNが大きすぎて間に合わない
# -> union findの気持ち
# 重み付きunionfindですべての重みを1にしておけば、重み=経路長になりそう?
# 駄目でした（そりゃそうだ よくよく考えたらa,bが途中で合流した場合にどちらもそのまま根にいってしまうのだから）
n = int(input())
parents = [i for i in range(n)]
weights = [0 for _ in range(n)]


def root(x):
    if x == parents[x]:
        return x
    y = root(parents[x])
    weights[x] += weights[parents[x]]
    parents[x] = y
    return y


def cost(x):
    # xからxの根までのコスト
    if x == parents[x]:
        return 0
    else:
        return weights[x] + cost(parents[x])


def same(a, b):
    return root(a) == root(b)


def unite(a, b):
    ra, rb = root(a), root(b)
    if b != rb:
        weights[ra] = 1 - cost(a)
    else:
        weights[ra] = 1 - (weights[a] - weights[b])
    parents[ra] = b


for i in range(n - 1):
    x, y = map(lambda x: int(x) - 1, input().split())
    if not same(x, y):
        unite(x, y)

q = int(input())
print(weights)
for _ in range(q):
    a, b = map(lambda x: int(x) - 1, input().split())
    print(cost(a) + cost(b) + 1)

"""
5
1 2
1 3
1 4
4 5
3
2 3
2 5
2 4

6
1 2
2 3
3 4
4 5
5 6
4
1 3
1 4
1 5
1 6
"""
