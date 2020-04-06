# 同じ字は最初のやつの最大値にひっぱられるのと、あとのやつの最小値にひっぱられる
# すげぇ雑に書いた
# なんかしらんけどいくつものケースでWAなるんだが????????????
n, m = map(int, input().split())
name = input()
kit = input()
named, kitd = {}, {}
for a in name:
    if a in named:
        named[a] += 1
    else:
        named[a] = 1
for a in kit:
    if a in kitd:
        kitd[a] += 1
    else:
        kitd[a] = 1
flag = False
maxk, maxv = list(named.keys())[0], 0
for k, v in named.items():
    if k not in kitd:
        flag = True
    if named[maxk] <= v:
        maxk = k
        maxv = v
if flag:
    print(-1)
    exit()
ans = maxv // kitd[maxk] if maxv / kitd[maxk] == maxv // kitd[
    maxk] else maxv // kitd[maxk] + 1
print(ans)