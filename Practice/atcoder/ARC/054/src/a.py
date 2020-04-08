# say ho きょり ＝ じかん かける はやさ
# 右or左回り どちらで行ったほうが早いか

l, x, y, s, d = map(int, input().split())
if s == d:
    print(0)
elif x == y:
    # 進むしかない
    if s < d:
        print((d - s) / (x + y))
    else:
        print((d + (l - s)) / (x + y))
elif x < y:
    if s < d:
        print(min((d - s) / (x + y), min(d - s, (s + (l - d))) / (y - x)))
    else:
        print(min((d + (l - s)) / (x + y),
                  min(s - d, (d + (l - s))) / (y - x)))
elif x > y:
    if s < d:
        print(min((d - s) / (x + y), min(d - s, (s + (l - d))) / (x - y)))
    else:
        # ここがあやしい
        # print(min((d + (l - s)) / (x + y),
        #           min(s - d, (d + (l - s))) / (x - y)))
        print((d + (l - s)) / (x + y))
