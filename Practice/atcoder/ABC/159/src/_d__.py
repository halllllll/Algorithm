# ncr再びって感じ(Aもncrだった)
# 登場回数が2以上のものが対象になる 多そうなのでncr自体をメモ化しておくか
# TLEくらった もうすこしメモ化してみる（どうせ同じ数があるのでncrの計算を減らすべく、答え自体をメモ化した(memo2)）
# それでもTLEくらった

n = int(input())
arr = list(map(int, input().split()))
memo = {}
memo2 = {}
dic = {}
for a in arr:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1


def ncr(n, r):
    # ささやかなメモ化
    if (n, r) in memo:
        return memo[(n, r)]
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    memo[(n, r)] = res
    return res


for a in arr:
    if a in memo2:
        print(memo2[a])
    else:
        ans = 0
        dic[a] -= 1
        for k, v in dic.items():
            if v > 1:
                ans += ncr(v, 2)
        print(ans)
        dic[a] += 1
        memo2[a] = ans
