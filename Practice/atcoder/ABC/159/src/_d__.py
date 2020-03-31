# ncr再びって感じ(Aもncrだった)
# 登場回数が2以上のものが対象になる 多そうなのでncr自体をメモ化しておくか
# TLEくらった もうすこしメモ化してみる（どうせ同じ数があるのでncrの計算を減らすべく、答え自体をメモ化した(memo2)）
# それでもTLEくらった
# あ クエリに対してあらかじめ答えを用意しておけばいいか
# なぜかWAくらったしTLEが直ってない

n = int(input())
arr = list(map(int, input().split()))
memo = {}

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


ans = {}
for k, v in dic.items():
    if k in ans:
        continue
    if v < 2:
        ans[k] = 0
        continue
    tmp = 0
    dic[k] -= 1
    for kk, vv in dic.items():
        if vv >= 2:
            tmp += ncr(vv, 2)
    dic[k] += 1
    ans[k] = tmp
for a in arr:
    print(ans[a])
