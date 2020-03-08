# 要素が3つあるかと思いきや評価方法はそれらの総和だけなので結局1つだけじゃんね
# と思ったら問題を読み違えていた 合計値の絶対値なので最後までわからんということか 最後までやってると当然間に合わない これどうすんの 前回の計算結果も流用できないのでは
# -> ぜんぶためす でした 死
# "8通り"?????「基準が正方向と負方向の2つで、3つの要素のうち1つの基準が決まれば残りも決まる」から6通りじゃね??????????????

# なぜか5WAなる..........は？？？？？？？？？？？？？？？？？

n, m = map(int, input().split())
dp = {}
beauties, yammies, favorities = [], [], []
for i in range(n):
    b, y, f = map(int, input().split())
    beauties.append([i, b])
    yammies.append([i, y])
    favorities.append([i, f])


def gen_indicies(base, reverse):
    return list(
        map(lambda x: x[0], sorted(base, key=lambda x: x[1], reverse=reverse)[:m])
    )


def sum_by_indicies(arr, indicies):
    ret = 0
    for i in indices:
        ret += arr[i][1]
    return ret


ans = -(10 ** 10)
# 綺麗さ降順
indices = gen_indicies(beauties, True)
b_tmp, y_tmp, f_tmp = (
    sum_by_indicies(beauties, indices),
    sum_by_indicies(yammies, indices),
    sum_by_indicies(favorities, indices),
)
ans = max(ans, abs(b_tmp) + abs(y_tmp) + abs(f_tmp))
# 綺麗さ昇順
indices = gen_indicies(beauties, False)
b_tmp, y_tmp, f_tmp = (
    sum_by_indicies(beauties, indices),
    sum_by_indicies(yammies, indices),
    sum_by_indicies(favorities, indices),
)
ans = max(ans, abs(b_tmp) + abs(y_tmp) + abs(f_tmp))
# 旨さ降順
indices = gen_indicies(beauties, True)
b_tmp, y_tmp, f_tmp = (
    sum_by_indicies(beauties, indices),
    sum_by_indicies(yammies, indices),
    sum_by_indicies(favorities, indices),
)
ans = max(ans, abs(b_tmp) + abs(y_tmp) + abs(f_tmp))
# 旨さ昇順
indices = gen_indicies(beauties, False)
b_tmp, y_tmp, f_tmp = (
    sum_by_indicies(beauties, indices),
    sum_by_indicies(yammies, indices),
    sum_by_indicies(favorities, indices),
)
ans = max(ans, abs(b_tmp) + abs(y_tmp) + abs(f_tmp))
# 人気さ降順
indices = gen_indicies(favorities, True)
b_tmp, y_tmp, f_tmp = (
    sum_by_indicies(beauties, indices),
    sum_by_indicies(yammies, indices),
    sum_by_indicies(favorities, indices),
)
ans = max(ans, abs(b_tmp) + abs(y_tmp) + abs(f_tmp))
# 人気さ昇順
indices = gen_indicies(beauties, False)
b_tmp, y_tmp, f_tmp = (
    sum_by_indicies(beauties, indices),
    sum_by_indicies(yammies, indices),
    sum_by_indicies(favorities, indices),
)
ans = max(ans, abs(b_tmp) + abs(y_tmp) + abs(f_tmp))
print(ans)
