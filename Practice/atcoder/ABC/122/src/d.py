# ちーともわからんので解説見た
# ら、悔しさあふれる感じ
# NGになる文字の並びは限定される。3文字のものは"ACG" "GAC", 4文字のものは"AxGC", "AGxC"
# ここで, "AAGC"とか"AGCC"なんてのを考え出すと「すでに"AGC"が含まれとるやんけ」->（だから何？）みたいなよくわからん思考に陥ってしまった
# （いまみてるのとそれ以前の3つを保存して探索すると結局かぶらず全探索できるので考えなくていい）

# n = input()

# なんで？？？？？？？？？？？
# これが無限ループになるの？？？？？？？？？？？？？？？？
# は？？？？？？？？？？？？？？？？？？？？？？？？？？？
# def f(i, s):
#     if i == n:
#         return 1
#     # print("now s : {}".format(s))
#     ret = 0
#     for c in "ACGT":
#         print(s + c)
#         is_include = True if "AGC" in s + c else False
#         if is_include:
#             continue
#         ret += f(i + 1, s[1:] + c)
#     return ret
# print(f(0, "xxx"))
# coding: utf-8
# Your code here!

n = int(input())
memo = {}


def f(i, s):
    if (i, s) in memo:
        return memo[(i, s)]
    if i == n:
        return 1
    ret = 0
    for c in "AGCT":
        flag = False
        for j in range(4):
            t = list(s + c)
            if j >= 1:
                t[j], t[j - 1] = t[j - 1], t[j]
            if "AGC" in "".join(t):
                flag = True
        if not flag:
            ret += f(i + 1, s[1:] + c)
            ret %= 10 ** 9 + 7
    memo[(i, s)] = ret
    return ret


print(f(0, "TTT"))
