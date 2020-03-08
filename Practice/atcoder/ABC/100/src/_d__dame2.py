# あれか 8通りのソート、同じ値があった場合に少しでも得られるポイントを高くするため、か？？？
n, m = map(int, input().split())
cakes = []
for _ in range(n):
    cakes.append(list(map(int, input().split())))

ans = -(10 ** 10)


def gen_tmp(lis):
    ret = sorted(cakes, key=lambda x: (x[0] * lis[0], x[1] * lis[1], x[2] * lis[2]))[:m]
    return ret


# 綺麗さ降順・旨さ降順・人気さ降順
# print("# 綺麗さ降順・旨さ降順・人気さ降順")

tmp = gen_tmp([-1, -1, -1])

b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
# 綺麗さ降順・旨さ降順・人気さ昇順
tmp = gen_tmp([-1, -1, 1])

b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
# 綺麗さ降順・旨さ昇順・人気さ降順


tmp = gen_tmp([-1, 1, -1])
b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
# 綺麗さ降順・旨さ昇順・人気さ昇順

tmp = gen_tmp([-1, 1, 1])
b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
# 綺麗さ昇順・旨さ降順・人気さ降順

tmp = gen_tmp([1, -1, -1])
b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
# 綺麗さ昇順・旨さ降順・人気さ昇順

tmp = gen_tmp([1, -1, 1])
b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
# 綺麗さ昇順・旨さ昇順・人気さ降順

tmp = gen_tmp([1, 1, -1])
b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
# 綺麗さ昇順・旨さ昇順・人気さ昇順

tmp = gen_tmp([1, 1, 1])
b, y, f = 0, 0, 0
for t in tmp:
    b += t[0]
    y += t[1]
    f += t[2]
ans = max(ans, abs(b) + abs(y) + abs(f))
print(ans)
