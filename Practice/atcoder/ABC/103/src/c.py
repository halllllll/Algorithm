# (lcm-1) % Ai なんだけどMLEなりそうな予感

from functools import reduce

n = int(input())
arr = list(map(int, input().split()))


def gcd(x, y):
    if x > y:
        return gcd(y, x)
    while x > 0:
        x, y = y % x, x
    return y


def lcm(x, y):
    return (x * y) // gcd(x, y)


x = reduce(lambda x, y: lcm(x, y), arr) - 1

ans = 0
for a in arr:
    ans += x % a
print(ans)
