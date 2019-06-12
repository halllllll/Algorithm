# それぞれソート済みとして, 整数でAi<BjかつBj<Ckとなるjを求める(にぶたん)

N = int(input())
A = list(sorted(list(map(int, input().split()))))
B = list(sorted(list(map(int, input().split()))))
C = list(sorted(list(map(int, input().split()))))


def lower_bound(arr, target):
    # targetを超える最小の値のインデックス
    if target > arr[-1]:
        return None
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return right


def upper_bound(arr, target):
    # target以上の最小の値のインデックス
    if target < arr[0]:
        return None
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return right


count = 0

for b in B:
    ai = upper_bound(A, b)
    ci = lower_bound(C, b)
    if ai is not None and ci is not None:
        count += ai * (N - ci)

print(count)
