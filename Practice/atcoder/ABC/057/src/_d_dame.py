# なんですかこの数学は
# 直感的には降順ソートしてA個が最大でいいんだけど、Bを使って(?)最大値になる組み合わせの総数を堪えるのがぜんぜんわからん
# とりあえず最後のサンプルのや Σ50C1~50C50だろこれ
# 平均を取るなら、降順で頭からとっていくとすると減っていく一方になる（多分）
# なので、「降順でA個目の登場回数どれをとるか」になるしかないんでは


def ncr(n, r):
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    return res


n, a, b = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
ans_a, ans_b = arr[0], 0
tmp_a = 0
minn_count = 0
for i in range(1, n):
    if i + 1 < a:
        ans_a += arr[i]
    elif i + 1 == a:
        ans_a += arr[i]
        ans_a /= a
        minn_count = 1
        tmp_a = arr[i]
    else:
        if tmp_a == arr[i]:
            minn_count += 1
        else:
            break
# minnCa~minnC[min(minnc, b)]みたいなもんか？（雑
print("minn_count: {}".format(minn_count))
for i in range(a, min(minn_count, b)):
    ans_b += ncr(minn_count, i)
print(ans_a)
print(ans_b)