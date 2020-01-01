# 問題文の意味はわからんけど（ちょうど1回、ちょうど2回割り切れる？？？？は？？？？？？？？）サンプルを適当に読む
d, n = map(int, input().split())
if d == 0:
    if n == 100:
        print(101)
    else:
        print(n)
elif d == 1:
    if n == 100:
        print(101 * 100)
    else:
        print(n * 100)
else:
    if n == 100:
        print(101 * 10000)
    else:
        print(n * 10000)

