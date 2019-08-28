# 一瞬「TiのうちSに含まれるものの個数」かと思って、「にぶたんでTi-1を超える最小のインデックスとTiを超える最小のインデックスの差をとればいけるかな」と思ってた
# 問題もっと単純で、ただ含まれてるかどうか判断するだけだった
# もちろんこんなことしなくても[値:個数]の連想配列を用意すれば事足りるんだけどな

n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))


def f(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        if target < arr[mid]:
            right = mid
        else:
            left = mid + 1
    return False


count = 0
for i in t:
    count += 1 if f(s, i) else 0
print(count)
