# ２次元配列バージョン
# かつ、内包表記バージョン
n = int(input())
suits = ["S", "H", "C", "D"]
cards = [[s, n] for s in suits for n in range(1, 14)]
for i in range(n):
    target = list(map(
        lambda a: int(a) if a.isnumeric() else a, input().split()
    ))
    if target in cards:
        cards.remove(target)
[print("{} {}".format(c[0], c[1])) for c in cards]
