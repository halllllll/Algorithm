# 差のリストをもっておいて、
# 前後で単調増加/減少する場所にきたら(行き帰りで)2倍して引く

n = int(input())
arr = list(map(int, input().split()))


def dif(arr):
    temp_arr = [0] + arr[:]
    res = []
    for i in range(1, len(temp_arr)):
        res.append(abs(temp_arr[i] - temp_arr[i - 1]))
    return res


lis = dif(arr)
s = sum(lis)+int(arr[-1])
for i in range(n):
    if i != 0 and i != n - 1:
        if arr[]
    else:
