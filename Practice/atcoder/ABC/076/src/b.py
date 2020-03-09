n, k = int(input()), int(input())


def rec(i, d):
    if i == n:
        return d
    return min(rec(i + 1, d + k), rec(i + 1, d * 2))


print(rec(0, 1))
