# ncrかなと思うが実験すると1 3 6 10 15 21みたいなのが出てくる
# あらかじめN個作っとくんだけどこれ間に合うん？
# 無理ですね はい  解説

# 愚直にみればそれぞれ選ぶか選ばないかで2通りがn回続く
# a,bの2数も含むとすると、すなわち、2^(n) - 1（かならず1本は選ぶので）。これは繰り返し二乗法で解く。
# ここからa,bを考えたものを引く。具体的にはnCr(n, a) mod p とnCr(n, b) mod pを引く。
# nCr mod pで間に合わんやんけと思って諦めたけどよくよく読んだら条件はa = min(n, 2*10^5)なので間に合うやんけ
# nCrの式変形で分母と分子をそれぞれ作ってやるっていう愚直なやつでもいけるんじゃねこれ
# Python3だとTLEなのでPypyでやった それでも1600msでヤバい どっか違うんだろうね しらんけど

n, a, b = map(int, input().split())
MOD = 10**9 + 7


# 繰り返し二乗法
def repMod(a, n, p):
    if n == 1:
        return a % p
    if n % 2 == 1:
        return a * repMod(a, n - 1, p) % p
    ret = repMod(a, n // 2, p) % p
    return (ret * ret) % p


all_comb = repMod(2, n, MOD)
# nCr = n!/(r!(n-r)!) ゆえ ((n-r+1) * (n-r+2) * .. * n)/(1*2*3*..*r)
# これがr = min(n, 2*10^5)なので愚直にやっても間に合う


def nCrMod(n, r, p):
    ret = 1
    # 分子
    for i in range(n - r + 1, n + 1):
        ret *= i
        ret %= p
    # 分母
    for i in range(2, r + 1):
        # ret //= i なんかこれがおかしい（なんでだろうね）
        ret *= repMod(i, p - 2, p)  # なぜかここでやらないと駄目だった
        ret %= p
    # ret = repMod(ret, p - 2, p) # なぜかここでやると駄目だった
    return ret % p


print((all_comb - nCrMod(n, a, MOD) - nCrMod(n, b, MOD) - 1) % MOD)
