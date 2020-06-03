import bisect
n = int(input())
arr = list(map(int, input().split()))
l = [10**8] * n
length = 1
for i in range(n):
    if arr[i] > l[length - 1]:
        l[length] = arr[i]
        length += 1
    else:
        idx = bisect.bisect_left(l, arr[i])
        l[idx] = arr[i]
print(length)