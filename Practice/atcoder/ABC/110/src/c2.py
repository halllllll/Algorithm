# きりみんちゃんの配信からきました
# 登場回数が同一ならいけそうなのでそうする
s, t = input(), input()
sd, td = {}, {}
for sv in s:
    if sv in sd:
        sd[sv] += 1
    else:
        sd[sv] = 1
for tv in t:
    if tv in td:
        td[tv] += 1
    else:
        td[tv] = 1
sort_sk, sort_tk = sorted(sd.values()), sorted(td.values())
print("Yes" if sort_sk == sort_tk else "No")