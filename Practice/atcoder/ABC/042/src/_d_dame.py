# 0<=y<h-bなるyを通るとこからゴールの右下までのnCrをする
# グリッドじゃなくてマス目にしただけでnCrわからなくなるの、あたまが弱すぎる
h, w, a, b = map(int, input().split())
ans = 0


def ncr(n, r):
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    return res


print(ncr(h + w, h))

for y in range(1, h - b + 1):
    ans += ncr(y, a) * ncr(w - a - 1 + h - b, w - a)
print(ans)

