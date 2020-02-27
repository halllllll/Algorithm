# 小さいのでメモ化再帰でいけるか？
# （[ここまでの回答数, ここまでの点数]みたいなやつ）
# んーーーーーー？？？？ RE*1、あとTLEになる。。。
# REはどうせ再帰の制限
# -> REからTLEになっただけだった
# そもそもこのメモ化は意味があるのか？消して試してみる
# -> あるっぽい 消すと5ACにしかならない

import sys

sys.setrecursionlimit(10 ** 8)

d, g = map(int, input().split())
memo = {}
points, bonus = [], []
for _ in range(d):
    p, c = map(int, input().split())
    points.append(p)
    bonus.append(c)


def f(c, p):
    if (c, p) in memo:
        return memo[(c, p)]
    if p >= g:
        return c
    ret = 10 ** 10
    for i in range(d):
        if points[i] == 1:
            points[i] = 0
            ret = min(ret, f(c + 1, p + (i + 1) * 100 + bonus[i]))
            points[i] = 1
        elif points[i] > 1:
            # 1つずつ減らすならいっそ全部減らしたほうがいい、らしい
            points[i] -= 1
            ret = min(ret, f(c + 1, p + (i + 1) * 100))
            points[i] += 1
        elif points[i] == 0:
            continue
        else:
            print(3 / 0)
    memo[(c, p)] = ret
    return ret


print(f(0, 0))
