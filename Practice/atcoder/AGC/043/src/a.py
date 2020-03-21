h, w = map(int, input().split())
table = [list(input()) for _ in range(h)]

dp = {}

# 最短で通ってるやつのうちの連続してる箇所


# Y, X, ひとつ前が#かどうか
def rec(y, x, f):
    if (y, x, f) in dp:
        return dp[(y, x, f)]
    if y == h - 1 and x == w - 1:
        return 0
    if y < 0 or h <= y or x < 0 or w <= x:
        print(10.0 / 0)
    ret = 10**8
    steps = [0, 1, 0]
    for i in range(2):
        next_x, next_y = x + steps[i], y + steps[i + 1]
        if 0 <= next_y < h and 0 <= next_x < w:
            if table[next_y][next_x] == "#":
                if f == True:
                    ret = min(rec(next_y, next_x, True), ret)
                else:
                    ret = min(rec(next_y, next_x, True) + 1, ret)
            else:
                ret = min(rec(next_y, next_x, False), ret)
        else:
            continue
    dp[(y, x, f)] = ret
    return ret


ans = rec(0, 0, True) + 1 if table[0][0] == "#" else rec(0, 0, False)
print(ans)
"""
問題文読み違えてた？
3 3
.##
#.#
#..
だと
2
じゃなくて
1
が正解？

ADD: やっぱり読み違えてたみたいだ 1時間以上ロスしたんだけど 日本語のおべんきょうをやりなおそうね
"""