# lower bound ...  「target以上となる最小の値」の場所


def lower_bound(arr, target):
    left, right = 0,  len(arr)
    while left < right:
        mid = (left + right)//2
        if arr[mid] >= target:  # upper_boundとはここが異なる
            right = mid
        else:
            left = mid + 1
    return right
