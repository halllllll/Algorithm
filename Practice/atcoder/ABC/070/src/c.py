# まあ最小公倍数lcmでしょう lcmのアルゴリズムはしらんけどたしかgcdを求めてからなんかするやつ

n = int(input())
x = int(input())


def gcd(x, y):
    if x > y:
        return gcd(y, x)
    while x != 0:
        x, y = y % x, x
    return y


def lcm(x, y):
    return (x*y)//gcd(x, y)


for _ in range(n - 1):
    y = int(input())
    x = lcm(x, y)

print(x)
