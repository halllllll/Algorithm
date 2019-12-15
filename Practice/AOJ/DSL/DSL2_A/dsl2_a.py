n, q = map(int, input().split())
INF = 2 ** 31 - 1
amount = 1
while amount < n:
    amount *= 2

# 初期値が決まっているので残念ながら初期化処理フェーズなし
arr = [INF for _ in range(2 * amount - 1)]


def update(t, v):
    # 全体で2N-1個で後半N個に最下部配列n個あるのでそれ以上はN-1個、
    # なので最下部配列の左側は添字N-1でアクセスできる
    t += amount - 1
    arr[t] = v
    while t > 0:
        # 親ノードのインデックスは（n-1)/2 （nは今いるノード番号）
        t = (t - 1) // 2
        # 子ノードのインデックスは 2*n+1（左側) と 2*n+2（右側）
        arr[t] = min(arr[2 * t + 1], arr[2 * t + 2])


# なんでlen(arr)じゃなくてamountなんだ？？？？？
def find(a, b, t=0, l=0, r=amount):
    # print("a, b, l, r, t = {}".format([a, b, l, r, t]))
    # 範囲外の場合 テキトーな値を返す
    if r <= a or b <= l:
        return INF
    # 覆っている場合 値を返せる
    if a <= l and r <= b:
        return arr[t]
    # 被っている場合 狭める
    lv = find(a, b, 2 * t + 1, l, (l + r) // 2)
    rv = find(a, b, 2 * t + 2, (l + r) // 2, r)
    return min(lv, rv)


for _ in range(q):
    query = list(map(int, input().split()))
    x, y = query[1:]
    if query[0] == 0:
        update(x, y)
    else:
        print(find(x, y + 1))
        print(arr)

