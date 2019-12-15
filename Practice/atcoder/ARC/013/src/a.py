# 全部試す
# p * qの面、q * rの面、r * pの面をそれぞれ下にしてn * mをはみ出さないように敷き詰めて高さもギリギリまで判定
n, m, l = map(int, input().split())
p, q, r = map(int, input().split())


def f(a, b, c):
    # a,bで底面、cは高さ
    w = n // a
    y = m // b
    z = l // c
    return w * y * z


print(max(f(p, q, r), f(p, r, q), f(q, r, p), f(q, p, r), f(r, p, q), f(r, p, q)))
