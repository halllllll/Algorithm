# 大方の予想通りにぶたんを都度やる+全探索
# （最初はクエリが飛んだときにO(1)なる方法があるのかと思ってたけどな）
# にぶたんでそこから右側と左側の直近にある寺と神社を同定して探索
# はーーーー？？？TLEなる....
# 単にPythonが遅いからでは？ちなPyPyでもTLE

a, b, q = map(int, input().split())
INF = 10 ** 18
s, t = (
    [-INF] + [int(input()) for _ in range(a)] + [INF],
    [-INF] + [int(input()) for _ in range(b)] + [INF],
)


def lower_bound(x, arr):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l


for _ in range(q):
    target = int(input())
    # print("target = {}".format(target))
    y = lower_bound(target, s)
    if y == a + 1:
        y -= 1
    elif y == 1:
        y += 1
    x = y - 1
    w = lower_bound(target, t)
    if w == b + 1:
        w -= 1
    elif w == 1:
        w += 1
    z = w - 1
    # print("based s: x, y={}, {}".format(x, y))
    # print("based t: z, w={}, {}".format(w, z))
    m = min(
        abs(target - s[x]) + abs(s[x] - t[w]),
        abs(target - s[x]) + abs(s[x] - t[z]),
        abs(target - s[y]) + abs(s[y] - t[w]),
        abs(target - s[y]) + abs(s[y] - t[z]),
        abs(target - t[z]) + abs(t[z] - s[x]),
        abs(target - t[z]) + abs(t[z] - s[y]),
        abs(target - t[w]) + abs(t[w] - s[x]),
        abs(target - t[w]) + abs(t[w] - s[y]),
    )
    print(m)
