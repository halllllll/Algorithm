# これ愚直じゃダメなのかな
# 上下左右それぞれのテーブルを用意し、いまいるところより上/下/左/右にいくつあるかをセーブする（自分は含まない）
# ↑ この4方向累積和方針はあってるっぽいけど愚直に4方向のテーブルを作ってみたいな方針でやったらTLEなった。あとは頼む
# ↑ やりました（4ヶ月ぶり） -> 駄目でした TLE
# ↑ pypyなら通りました なんだって
h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(input()))

toR, toL = (
    [[0 for _ in range(w + 1)] for _ in range(h)],
    [[0 for _ in range(w + 1)] for _ in range(h)],
)
toU, toD = (
    [[0 for _ in range(w)] for _ in range(h + 1)],
    [[0 for _ in range(w)] for _ in range(h + 1)],
)


for y in range(h):
    for x in range(w):
        if grid[y][x] == ".":
            toR[y][x + 1] += toR[y][x] + 1
            toD[y + 1][x] += toD[y][x] + 1
        else:
            toR[y][x + 1] = 0
            toD[y + 1][x] = 0

        if grid[y][w - x - 1] == ".":
            toL[y][w - x - 1] += toL[y][w - x] + 1
        else:
            toL[y][w - x - 1] = 0

        if grid[h - y - 1][x] == ".":
            toU[h - y - 1][x] += toU[h - y][x] + 1
        else:
            toU[h - y - 1][x] = 0

ans = 0
for y in range(h):
    for x in range(w):
        tmp = toR[y][x + 1] + toL[y][x] + toD[y + 1][x] + toU[y][x] - 3
        ans = max(ans, tmp)

print(ans)

