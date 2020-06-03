# ソートして左右からとっていくが、可能ならば同じ数字が連続しないようにする
# めんどいわ なーにが「可能ならば」じゃ
# 左右どちらを先にとるかでいいんじゃないの
# -> だめでした
# 理屈はわからんが、最後のやつを最初にもっていくやつが浮かんだがなんだこれ
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)


def f(arr):
    ans = []
    c, l, r = 0, 0, n - 1
    while c < n:
        if c % 2 == 0:
            ans.append(arr[l])
            l += 1
        else:
            ans.append(arr[r])
            r -= 1
        c += 1
    ans = [ans[-1]] + ans[:-1]
    result, tmp = 0, ans[0]
    for i in range(1, n):
        result += abs(tmp - ans[i])
        tmp = ans[i]
    return result


a, b = f(arr), f(list(reversed(arr)))
print(max(a, b))
