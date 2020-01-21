# 最小公倍数を目指す？
n = int(input())
arr = list(map(int, input().split()))


def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


def lcm(a, b):
    ret = (a * b) // gcd(a, b)
    # ret = ret % (10 ** 9 + 7)  # これがめっちゃ怖い TLEなりそう.. でもどうすんだ...
    return ret


a = arr[0]
for i in range(1, n):
    a = lcm(a, arr[i])
ans = 0
for av in arr:
    z = a // av  # % (10 ** 9 + 7)
    ans += z
    # ans %= 10 ** 9 + 7
print(ans % (10 ** 9 + 7))
