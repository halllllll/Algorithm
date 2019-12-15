# 超特殊なにぶたんを作る

a, b, x = map(int, input().split())


def keta(x):
    c = 0
    while x > 0:
        x //= 10
        c += 1
    return c


def super_nibutan(a, b, x):
    l, r = 0, x
    while l < r:
        # print("l, r = {}, {}".format(l, r))
        mid = (l + r) // 2
        if a * mid + b * keta(mid) > x:
            r = mid
        else:
            l = mid + 1
    l -= 1
    # print(
    #     "a*n + b*d(n) = {} * {} + {} * {} = {}".format(
    #         a, l, b, keta(l), a * l + b * keta(l)
    #     )
    # )
    return min(l, 10 ** 9)


print(super_nibutan(a, b, x))
