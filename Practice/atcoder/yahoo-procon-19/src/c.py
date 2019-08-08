# ほしいのは枚数なので、円は必要ない。円が使えるなら使ったほうがいい
# なぜかうまくいかない....
# dpを使うか
# dpでも間に合わないのでおそらくサクッと計算する方法があるっぽい

import sys

sys.setrecursionlimit(10 ** 6)

k, A, B = map(int, input().split())
dp = {}


def f(k, b, y):
    # まずはいつもどおり再帰で
    if (k, b, y) in dp:
        return dp[(k, b, y)]
    ret = 0
    if k == 0:
        ret = b
    if y == 0:
        if b >= A:
            ret = max(f(k - 1, b - A, y + 1), f(k - 1, b + 1, y))
        else:
            ret = f(k - 1, b + 1, y)
    else:
        ret = max(f(k - 1, b + B, y - 1), f(k - 1, b + 1, y))
    dp[(k, b, y)] = ret
    return ret


print(f(k, 1, 0))
