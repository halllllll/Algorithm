# サンキューsample3
# dの偶奇で行ける場所がわかる あとは範囲
r, c, d = map(int, input().split())
evens, odds = [], []
for ri in range(r):
    line = list(map(int, input().split()))
    for ci in range(c):
        if ri + ci > d:
            break
        if (ri + ci) % 2 == 0:
            # どうがんばっても初期値からの距離が偶数の場所しかいけない
            evens.append(line[ci])
        else:
            # 同じく奇数の場所
            odds.append(line[ci])
print(max(evens) if d % 2 == 0 else max(odds))
