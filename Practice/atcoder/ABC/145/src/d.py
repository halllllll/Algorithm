# nCr
# 駄目な場合を考える
# - x+yが3の倍数でない
# - min(x,y):max(x,y)が倍より大きい
x, y = map(int, input().split())
if (x + y) % 3 != 0 or (min(x, y) / max(x, y)) > 2.0:
    print(0)
    exit()

# なぜかいつものこれだと99999で違った出力になりWAなる
# def nCr(n, r):
#     res = 1
#     for i in range(1, r + 1):
#         res = res * (n - i + 1) // i
#         res %= 10 ** 9 + 7
#     return res


# x, yがそれぞれ何回ずつ2と1を使うか -> 片方が決まれたば一意に定まる
# 適当な連立方程式
n = (x + y) // 3
p = (n - abs(x - y)) // 2
# print(n, p)
# print(nCr(n, p))


# なんでWAになるんだろうね ググった


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10 ** 9 + 7  # 出力の制限
N = 10 ** 6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

print(cmb(n, p, mod))
