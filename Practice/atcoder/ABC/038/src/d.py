# 二次元LIS（二次元じゃない）
import bisect
n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr = sorted(arr, key=lambda x: x[1], reverse=True)
arr = list(map(lambda x: x[1], sorted(arr, key=lambda x: x[0])))

l = [10**10] * n
length = 1

for i in range(n):
    if arr[i] > l[length - 1]:
        l[length] = arr[i]
        length += 1
    else:
        idx = bisect.bisect_left(l, arr[i])
        l[idx] = arr[i]
print(length)
