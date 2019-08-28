# 逆に公倍数を引く。B-A+1-(Cの倍数の数+Dの倍数の数-CとDの公倍数の数)
a, b, c, d = map(int, input().split())


def gcd(x, y):
    if x > y:
        return gcd(y, x)
    while x > 0:
        x, y = y % x, x
    return y


def lcm(x, y):
    return (x * y) // gcd(x, y)


aa = (a - 1) - ((a - 1) // c + (a - 1) // d - (a - 1) // lcm(c, d))
bb = b - (b // c + b // d - b // lcm(c, d))
print(bb-aa)
