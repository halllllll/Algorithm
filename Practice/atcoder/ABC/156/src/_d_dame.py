n, a, b = map(int, input().split())


def ncr(n, r):
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
        res %= 10 ** 9 + 7
    return res


def myPow2(a, n):
    x = 1
    while n > 0:
        if n & 1:
            x = x * a
            x %= 10 ** 9 + 7
        a = a * a
        a %= 10 ** 9 + 7
        n >>= 1
    return x


av = ncr(n, a)
bv = ncr(n, b)
ans = myPow2(2, n) - 1
x = ans - av - bv
if x < 0:
    x += 10 ** 9 + 7
print(x % (10 ** 9 + 7))

