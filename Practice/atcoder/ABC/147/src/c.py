# 2**15=32000ちょいなのであらかじめ誰が正直者で誰がそうでないかのテーブルを作成し、それをもとにして探索。
# 矛盾がないことを探索していくような判定とデータ構造が浮かばん
# 正直者と、真偽不明の人、というのが味噌 嘘つきではない
# bit操作がわからんので配列でやった
# まじで判定とデータ構造どうすっかわからん

n = int(input())
syougen = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        syougen[i].append((x - 1, y))


def f(n, cur=[]):
    # 1と0からなる長さNの組み合わせを全2**n個出すジェネレータ
    if len(cur) == n:
        yield cur
    else:
        for i in range(2):
            _next = cur[:]
            _next.append(i)
            yield from f(n, _next)


def check(arr):
    for i in range(n):
        if arr[i] == 0:
            continue
        for x, y in syougen[i]:
            if arr[x] == 1 and y == 0:
                return False
            if arr[x] == 0 and y == 1:
                return False
    return True


ans = 0
for g in f(n):
    if check(g):
        ans = max(ans, sum(g))
print(ans)
