# 長さでまとめるか 複数一致する場合あると思うけどとくに条件に書かれてないから無視する
s = input().split()
n = int(input())
d = {}
for _ in range(n):
    x = input()
    lnh = len(x)
    if lnh in d:
        d[lnh].append(x)
    else:
        d[lnh] = [x]
ans = []
for c in s:
    x = len(c)
    tmp = c
    if x in d:
        for dif in d[x]:
            f = True
            for i in range(x):
                if dif[i] != "*" and c[i] != dif[i]:
                    f = False
            if f:
                tmp = "*" * len(dif)
        ans.append(tmp)
    else:
        ans.append(c)

print(" ".join(ans))