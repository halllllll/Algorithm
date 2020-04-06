# 最小値は見た感じ小さい順に解くとよさそうだしソートで累積和でsumでよさそう、種類は同じ時間かかるならどれを選んでもいいのでそれぞれの登場回数を掛ける
# 登場回数をかける、じゃなかったわ 登場回数ごとに階乗だわ 間に合うか？まあいいっしょ
n = int(input())
t, d = [], {}
for _ in range(n):
    x = int(input())
    t.append(x)
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
t = sorted(t)
ans1 = t[0]
for i in range(n - 1):
    t[i + 1] += t[i]
    ans1 += t[i + 1]
ans2 = 1
for v in d.values():
    for vv in range(v, 0, -1):
        ans2 *= vv
        ans2 %= (10**9 + 7)
print(ans1)
print(ans2)
