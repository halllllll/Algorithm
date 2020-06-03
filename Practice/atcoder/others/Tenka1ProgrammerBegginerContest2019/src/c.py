# 最終形態は...か###か....####
# 一つでも #. のセットがある場合はいっそ.か#をぜんぶ入れ替えるほうがいいかどうかっていう
# 無限にWAなるんだけどなんでこれがダメなのか納得いかない（解説は見たが納得がいかない
# ↑ なーにいってんだ 次の場合にダメじゃねぇか（3になった）
# 8
# ##..#..#
n, s = int(input()), input()
flag = True
for i in range(1, n):
    if s[i - 1] == "#" and s[i] == ".":
        flag = False
        break
if flag:
    print(0)
else:
    b = len(list(filter(lambda x: x == "#", s)))
    # 後ろの部分は黒関係ない
    countb = 0
    for bi in s[::-1]:
        if bi == "#":
            countb += 1
        else:
            break
    w = n - b
    countw = 0
    # 前の部分は白関係ない
    for wi in s:
        if wi == ".":
            countw += 1
        else:
            break
    print(min(w - countw, b - countb))
