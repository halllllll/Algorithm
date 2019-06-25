# ほしいのは枚数なので、円は必要ない。円が使えるなら使ったほうがいい
# なぜかうまくいかない....

k, a, b = map(int, input().split())
bisquet, yen = 1, 0

while k > 0:
    k -= 1
    if yen > 0:
        yen -= 1
        bisquet += b
    elif yen == 0 and bisquet >= a:
        bisquet -= a
        yen += 1
    else:
        bisquet += 1
    print("now bisquet: {} yen: {}".format(bisquet, yen))

print(bisquet)
