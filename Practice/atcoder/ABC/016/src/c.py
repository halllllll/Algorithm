# 深さ2までdfsすりゃいいか
# とか思ってたらなんかうまくいかなくて、原因はふたつあることに気づいて、
# 1. 友達の友達だと思ったら友達の場合がある
# 2. 問題の読み違え（「友達の友達」に至るパスではなく、その数そのものを答えるやつだった
# で30分くらい無駄にした気がする あたまがわるいからだね


n, m = map(int, input().split())
table = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    table[a - 1].append(b - 1)
    table[b - 1].append(a - 1)


def dfs(i, used, find):
    if len(used) == 3:
        # 判定
        first, last = used[0], used[-1]
        if first not in table[last] and last not in find:
            find.append(last)
            return 1
        else:
            return 0
    ret = 0
    for j in table[i]:
        if j not in used:
            next_used = used[:]
            next_used.append(j)
            ret += dfs(j, next_used, find)
    return ret


for i in range(n):
    print(dfs(i, [i], []))
