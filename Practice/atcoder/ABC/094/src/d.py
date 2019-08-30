# nCr的にn//2に近いほうがいいに決まっている
#

n = int(input())
arr = list(sorted(list(map(int, input().split()))))


def ncr(n, r):
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    return res


def lower_bound(arr, t):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > t:
            r = mid
        else:
            l = mid + 1
    return r


def upper_bound(arr, t):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= t:
            r = mid
        else:
            l = mid + 1
    return r


lb, up = lower_bound(arr)
