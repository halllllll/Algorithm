# nCr的にn//2に近いほうがいいに決まっている
# まあnCrは計算しなくていい

n = int(input())
arr = sorted(list(map(int, input().split())))


def lower_bound(arr, t):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < t:
            l = mid + 1
        else:
            r = mid
    return l


lb = lower_bound(arr[:-2], round(arr[-1] / 2))
lb_left = max(0, lb - 1)
if abs(round(arr[-1] / 2) - arr[lb]) >= abs(round(arr[-1] / 2) - arr[lb_left]):
    print(arr[-1], arr[lb_left])
else:
    print(arr[-1], arr[lb])
