# ２次元配列バージョン
# あらかじめ空の配列を用意しておくバージョン
n = int(input())
suits = ["S", "H", "C", "D"]
cards = []
for s in suits:
    for x in range(1, 14):
        cards.append([s, x])
for i in range(n):
    e = [int(l) if l.isnumeric() else l for l in input().split()]
    if e in cards:
        cards.remove(e)

for c in cards:
    print("{} {}".format(c[0], c[1]))
