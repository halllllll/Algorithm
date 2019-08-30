n = int(input())
h = list(map(int, input().split()))

global count
count = 0


def f(l, r, arr):
    # l以上r未満の範囲で探索
    global count
    while len(arr[l:r]) > 0 and all(arr[l:r]) and l < r:
        # l からrまですべて1以上のときはデクリメントし続ける
        arr = [a-1 if l <= idx and idx < r else a for idx, a in enumerate(arr)]
        count += 1
    # すべてが0だったら終了
    if sum(arr) == 0:
        return
    # l以上r未満のどっかに0が含まれるので、含まれない範囲を抽出
    if arr[0] > 0:
        # 左端がl、以後0が見つかったらr, なかったら右端
        r = arr.index(0) if 0 in arr else len(arr)
        f(0, r, arr)
    elif arr[0] == 0:
        # 左から数えて最初に1以上のインデックスがl、その次の0もしくは右端がr
        a, b = -1, len(arr)
        for idx, x in enumerate(arr):
            if x == 0 and a > 0:
                b = idx
                break
            if x > 0 and a < 0:
                a = idx
        f(a, b, arr)


f(0, n, h)
print(count)
