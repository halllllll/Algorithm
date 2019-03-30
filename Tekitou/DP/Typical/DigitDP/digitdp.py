# nが与えれるのでn以下の非負数を数えてみる, をdpでやる
# いつもどおりdpはメモ化再帰でやるんだよ
# これもいつもどおり、最初からやってもどうせわからんので
# 再帰つくってからやるんだよ

n = "59553"


def rec_non_memo(i, boolean):
    if i == len(n):
        return 1
    else:
        ret = 0
        limit = int(n[i]) if boolean is True else 9
        for j in range(limit + 1):
            nex_boolean = j <= limit and boolean is True
            ret += rec_non_memo(i+1, nex_boolean)
        return ret


print(rec_non_memo(0, True))

print("-" * 40)
# -----------------------------------------
# 例題 a
import time

n, d = "4945835", "24"
print('\033[32m' + "{}以下の整数のうち各桁の数の総和が{}になるものの総数".format(n, d) + '\033[0m')

print("---- メモ化なしバージョン ----")

"""
def rec_a(i, b, s):
    if i == len(n):
        # 最後の桁まできたら判定
        if s == int(d):
            return 1
        else:
            return 0
    if s > int(d):
        return 0
    ret = 0
    limit = int(n[i]) if b else 9
    for j in range(limit + 1):
        nex_b = j == limit and b
        ret += rec_a(i + 1, nex_b, s + j)
    return ret


starttime = time.perf_counter()
print(rec_a(0, True, 0))
endtime = time.perf_counter()
print("実行時間: {}".format(endtime-starttime))
"""
print("---- メモ化バージョン ----")


memo = [[[None for _ in range(int(d)+1)] for _ in range(2)]
        for _ in range(len(n)+1)]


def rec_a_memo(i, b, s):
    if i == len(n):
        return 1 if s == int(d) else 0
    if s > int(d):
        return 0
    if memo[i][b][s] is not None:
        return memo[i][b][s]

    ret = 0
    limit = int(n[i]) if b == 1 else 9
    for j in range(limit + 1):
        nex_b = 1 if (j == limit and b == 1) else 0
        ret += rec_a_memo(i + 1, nex_b, s + j)
        memo[i][b][s] = ret
    return ret


starttime = time.perf_counter()
print(rec_a_memo(0, 1, 0))
endtime = time.perf_counter()
print("実行時間: {}".format(endtime-starttime))

# 例題 b
n, a, b = "4954850", "3", "7"

print('\033[32m' +
      "{}以下の整数のうちいずれかの桁に{}と{}のいずれかが含まれる数の総和".format(n, a, b) + '\033[0m')

"""
print("---- 愚直バージョン（答え同定用） ----")
ans = 0
for i in range(int(n) + 1):
    ni = str(i)
    if a in ni or b in ni:
        ans += 1
print(ans)
"""
print("---- 再帰バージョン（非メモ） ----")


def rec_b(i, threshold, f):
    if i == len(n):
        return f
    ret = 0
    limit = int(n[i]) if threshold == 1 else 9
    for j in range(limit + 1):
        nex_thresold = 1 if (j == limit and threshold == 1) else 0
        nex_f = 1 if (f or str(j) in [a, b]) else 0

        ret += rec_b(i + 1, nex_thresold, nex_f)
    return ret


starttime = time.perf_counter()
print(rec_b(0, 1, 0))
endtime = time.perf_counter()
print("実行時間: {}".format(endtime - starttime))
print("---- メモ化バージョン ----")
memo = [[[None for _ in range(2)] for _ in range(2)]
        for _ in range(len(n) + 1)]


def rec_b_memo(i, threshold, f):
    if i == len(n):
        return f
    if memo[i][threshold][f] is not None:
        return memo[i][threshold][f]
    ret = 0
    limit = int(n[i]) if threshold == 1 else 9
    for j in range(limit + 1):
        nex_threshold = 1 if (j == limit and threshold == 1) else 0
        nex_f = 1 if (f or str(j) in [a, b]) else 0
        ret += rec_b_memo(i + 1, nex_threshold, nex_f)
        memo[i][threshold][f] = ret
    return ret


starttime = time.perf_counter()
print(rec_b_memo(0, 1, 0))
endtime = time.perf_counter()
print("実行時間: {}".format(endtime-starttime))
