# 1の出てくる位置で余計に一回探索するかどうか

n, k = map(int, input().split())
arr = list(map(int, input().split()))
idx = arr.index(1)
if idx + 1 <= k or n - k < idx + 1:
    print(round((n-1)/(k-1)))
else:
    print(round((n-1)/(k-1)))
