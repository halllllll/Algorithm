# 全然わからんかったので解答みたら最も短い辺をにぶたんで探すらしい
#
n = int(input())
arr = sorted(list(map(int, input().split())))
print(arr)


def super_nibutan(arr, t):
    l, r = 0, len(arr)


for i in range(n - 1, -1, -1):
    for j in range(i, -1, -1):
        if i == j:
            continue
        print(i, j)

