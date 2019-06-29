# ncrをうまく使う感じ 二項定理は実装がわかんなかったのでググってパクった

from math import factorial

n, k = map(int, input().split())
nn = n - k + 1  # 使える箇所


def ncr(n, r):
    res = 1
    for i in range(1, r+1):
        res = res * (n-i+1)//i
    return res


def calc(k):
    return [factorial(k)//(factorial(i)*factorial(k-i)) for i in range(k+1)]


nikouteiri = calc(k-1)

for i in range(1, k + 1):
    # 使える箇所からi個とり、kをi個のグループに分けたやつをかける
    print((ncr(nn, i) * nikouteiri[i-1]) % (10**9+7))
