# Nが非常に小さいけどそういうタイプのにぶたんなのかもしれない（オーバーキルか？）
from math import ceil
n, m = map(int, input().split())
name = input()
kit = input()
dic_name, dic_kit = {}, {}
for a in kit:
    if a not in dic_kit:
        dic_kit[a] = 1
    else:
        dic_kit[a] += 1
for a in name:
    if a not in dic_kit:
        print(-1)
        exit()
    if a not in dic_name:
        dic_name[a] = 1
    else:
        dic_name[a] += 1

l, r = 0, 51
while r - l > 1:
    mid = (r + l) // 2
    tmp = 1
    for av, ak in dic_name.items():
        if ak > dic_kit[av]:
            # print("必要な{}の数: {}".format(av, ceil(ak / dic_kit[av])))
            tmp = max(tmp, ceil(ak / dic_kit[av]))
    if tmp < mid:
        r = mid
    else:
        l = mid
print(l)