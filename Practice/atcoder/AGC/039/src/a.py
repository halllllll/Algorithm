# 先頭と末尾が同じ場合はそれを省き、単体で完結するもの*K + 先頭と末尾が同じ場合の連結部分 * (K-1)
# ただし全部同じ場合は別で計算
# 3WA出した後にtestcase: aaaeiiiaiaa でやって気づいた
# -> なーにが気づきじゃ なんも変わっとらんやんけ
# *(k-1) 忘れてたっぽい？
from math import floor

s = input()
k = int(input())
if len(set(list(s))) == 1:
    print(floor((len(s) * k) / 2))
    exit()

if s[0] == s[-1]:
    # このへんの算数は手書きでいくつか書いて帰納的に導出した
    # だるいしs<=100なので愚直に数えるわ
    pre, suf = 0, 0
    for c in s:
        if c == s[0]:
            pre += 1
        else:
            break
    for c in s[::-1]:
        if c == s[-1]:
            suf += 1
        else:
            break
    # 先頭と末尾の連続する文字を除いたやつのうち連続するやつからいらないやつを数える
    idx = 0
    cc = 0
    t = s[pre : len(s) - suf]
    while idx < len(t):
        c = 0
        tmp = idx
        while tmp < len(t) and t[tmp] == t[idx]:
            tmp += 1
            c += 1
        if c > 1:
            cc += floor(c / 2)
        idx = tmp
    ans = floor(pre / 2) + cc * k + floor((pre + suf) / 2) * (k - 1) + floor(suf / 2)
    print(ans)
else:
    idx = 0
    cc = 0
    t = s[:]
    while idx < len(t):
        c = 0
        tmp = idx
        while tmp < len(t) and t[tmp] == t[idx]:
            tmp += 1
            c += 1
        if c > 1:
            cc += floor(c / 2)
        idx = tmp
    ans = cc * k
    print(ans)
