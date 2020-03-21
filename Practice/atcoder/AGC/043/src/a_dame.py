h, w = map(int, input().split())
table = [list(input()) for _ in range(h)]

dp = {}


# Y, X, （使った）Count
def rec(y, x, c):
    if (y, x, c) in dp:
        return dp[(y, x, c)]
    if y == h - 1 and x == w - 1:
        dp[(y, x, c)] = c
        return c
    if y < 0 or h <= y or x < 0 or w <= x:
        print(10.0 / 0)
    ret = 10**8
    steps = [0, 1, 0]
    for i in range(2):
        next_x, next_y = x + steps[i], y + steps[i + 1]
        if 0 <= next_y < h and 0 <= next_x < w:
            if table[next_y][next_x] == "#":
                ret = min(rec(next_y, next_x, c + 1), ret)
            else:
                ret = min(rec(next_y, next_x, c), ret)
        else:
            continue
    dp[(y, x, c)] = ret
    return ret


print(rec(0, 0, 0))
