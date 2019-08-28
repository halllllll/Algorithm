# upper bound ...  「targetを超える最小の値」の場所


def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right)//2
        if arr[mid] > target:  # lower_boundとはここが異なる
            right = mid
        else:
            left = mid + 1
    return right
