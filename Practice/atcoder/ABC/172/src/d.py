n = int(input())
table = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    # こいつが地獄のように遅い
    # for v in tes.values():
    #     tmp *= (v + 1)
    # print(i, tmp)
    # 1からnまでの約数の個数を数えるズバリのやつがあるらしい エラトステネスを使ってるらしい
    # http://sucrose.hatenablog.com/entry/2016/11/06/234635
    for j in range(i, n + 1, i):
        table[j] += 1
for i in range(1, n + 1):
    ans += i * table[i]
print(ans)