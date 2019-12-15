def gcd(x, y):
    if x > y:
        return gcd(y, x)
    elif x == 0:
        return y
    x, y = y % x, x
    return gcd(x, y)


def lcm(x, y):
    return int((x * y) / gcd(x, y))


# try~except使うのあほくさい なんとかならんか
while True:
    try:
        get = list(map(int, input().split()))
        x, y = get
        print("{} {}".format(gcd(x, y), lcm(x, y)))
    except:
        break
