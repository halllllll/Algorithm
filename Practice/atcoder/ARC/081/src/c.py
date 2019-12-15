# 逆順ソートして辞書にして大きい順に2つ以上ある数値を2つとるか4つ以上ある数値をとればおしまい
# atcoderのPytnon3バージョンが時代錯誤すぎて辞書順の順番を保持しない老害仕様だったので6WAくらい喰らった
# 方針を変えて二回ループして全探索することにした

n = int(input())
arr = list(map(int, input().split()))
h = {}
for a in arr:
    if a in h:
        h[a] += 1
    else:
        h[a] = 1
x, y = 0, 0
tmp_ans = 0
for k, v in h.items():
    if 4 <= v:
        tmp_ans = max(tmp_ans, k * k)

for k, v in h.items():
    if 2 <= v:
        if x == 0 and y == 0:
            x = k
        elif x != 0 and y == 0:
            x, y = min(x, k), max(x, k)
        else:
            if y < k:
                x, y = y, k
    tmp_ans = max(tmp_ans, x * y)

print(tmp_ans)

