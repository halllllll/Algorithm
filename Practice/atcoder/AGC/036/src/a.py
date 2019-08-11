# 合成数なら(0,0)(a, 0)(a, b)で(a*b)/2==s/2なる。

s = int(input())


def f(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return i
    return 1


a = f(s)
b = (s // a) * 2
print("0 0 {} 0 {} {}".format(a, a, b))

