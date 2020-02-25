# はじめての三分探索
# y = x + p/(2^(x/1.5))
# こういう探索は適当な回数回す
# うーん わかんなくて写経したけどやっぱサクッとは書けん
# （まずx+p/(2^(x/1.5))の導出がむずい)

p = float(input())
l, r = 0.0, 100.0


def takahashiman(x):
    return x + p / (2 ** (x / 1.5))


for i in range(300):
    mid_left = (2.0 * l + r) / 3.0
    mid_right = (l + 2.0 * r) / 3.0
    t1 = takahashiman(mid_left)
    t2 = takahashiman(mid_right)
    if t1 >= t2:
        l = mid_left
    else:
        r = mid_right
print(takahashiman(r))
