# 愚直のやり方がわからんので頭を使う
# あとのやつが優先される->後ろから並べればいいのでは
# 同じのを動かす場合がある->後ろからみて動かしたものを優先にして、すでに出たものは（つまり先に動かしたものは）無視、最後にまだ出てきてないやつを昇順に並べる
n, m = map(int, input().split())
gets = [int(input()) - 1 for _ in range(m)][::-1]

used = [False for _ in range(n)]
for g in gets:
    if used[g] == False:
        print(g + 1)
        used[g] = True
for i in range(n):
    if used[i] == False:
        print(i + 1)
