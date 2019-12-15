# lower_bound バージョン

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
c = 0


def nibutan(arr, t):
    l, r = 0, len(arr)
    while l < r:
        mid = (r + l) // 2
        if arr[mid] >= t:
            r = mid
        else:
            l = mid + 1
    return arr[r]


for t in list(map(int, input().split())):
    ni = nibutan(arr, t)
    if ni == t:
        c += 1

print(c)
