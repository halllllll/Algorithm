# h*wのマスにかかれているそれぞれの数字の位置は関係ないしどうでもいい
# それぞれの数がどれだけあるかに興味がある
# iから1に至る最小値を全探索 間に合うのか？ まあいけるやろ
# Pythonだと間に合わず pypyだと間に合った。。。
# 解答みたらワーシャルフロイド使うらしい は？

h, w = map(int, input().split())
table = []
for _ in range(10):
    table.append(list(map(int, input().split())))

wall = {}
for _ in range(h):
    x = list(map(int, input().split()))
    for v in x:
        if v not in wall:
            wall[v] = 1
        else:
            wall[v] += 1


def rec(idx, cost, used):
    if idx == 1:
        return cost
    ret = 10 ** 10
    for i in range(10):
        if i in used:
            continue
        next_used = used[:]
        next_used.append(i)
        ret = min(ret, rec(i, cost + table[idx][i], next_used))
    return ret


arr = [0 for _ in range(10)]
for i in range(10):
    if i == 1:
        continue
    arr[i] = rec(i, 0, [i])

ans = 0
for k, v in wall.items():
    if k != -1 and k != 1:
        ans += arr[k] * v
print(ans)
