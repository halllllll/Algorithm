# どうしても1WAがとれない................................................................
# 鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱鬱


# 3パターンある
# 1. a < c < b < d
# 2. a < b < c < d
# 3. a < b < d < c
# 1はa-cとb-dで独立して考える それぞれの間に#が連続してなかったらおｋ
# 2はb-dが成功したあとa-cが成功すればおｋ
# 3はa-cが成功すればおｋ
# という考察を深めると、cとdの位置関係だけに注目すればいいことがわかる（わかる？）
# d < cのとき、aがcにいくためにbを飛び越えなければならない。飛び越えるには"..."の真ん中を避難地帯としてbを置くしかない

n, a, b, c, d = map(int, input().split())
s = list(input())
if c < d:
    if "##" not in "".join(s[a - 1 : c]) and "##" not in "".join(s[b - 1 : d]):
        print("Yes")
    else:
        print("No")
else:
    # aがゴールできる -> bがゴールできる（aの通る経路はすべてbも通るので）
    # bがゴールできる -> bのゴール後、aがゴールできるとは限らない
    tmp_s = s[:]
    tmp_s[d - 1] = "#"
    if ("##" not in "".join(s[a - 1 : c]) and "..." in "".join(s[b - 1 : d])) or (
        "##" not in "".join(tmp_s[a - 1 : c])
    ):
        print("Yes")
    else:
        print("No")
