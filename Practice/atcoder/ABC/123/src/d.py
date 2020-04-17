# は？なんやこれ無限にわからん
# 半分全列挙的な気持ちでやる？どうせKまでなので上位3000くらいでいいのと、AとBの和の降順ソートした上位Kは必ずAとBとCの和の降順ソートの上位K以内に含まれる
# -> Python3だと無理だった Pypyでいけた
x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ab = []
for av in a:
    for bv in b:
        ab.append(av + bv)
ab = sorted(ab, reverse=True)[:k]
abc = []
for abv in ab:
    for cv in c:
        abc.append(abv + cv)
abc = sorted(abc, reverse=True)[:k]
for ans in abc:
    print(ans)
