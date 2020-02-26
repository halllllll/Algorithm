# [n-l-1]からそれ以前l個ぶんだけみればよさそう?
# tmpを更新する時に二番目に小さい値にする
# 優先度つきキューでやってみる

import heapq

n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 1:
    arr = map(str, arr)
    print(" ".join(arr))
    exit()

r = 0
ans = []
tmp = 10 ** 14
second = 10 ** 14
a = []

for l in range(n):
    if r == n:
        break
    while r < n and r - l < k:
        heapq.heappush(a, [arr[r], r])
        r += 1
    print("arr {}".format(arr[l:r]))
    print("heap arr: {}".format(a))

    smallest = heapq.heappop(a)
    if tmp >= smallest:
        tmp = smallest
        print("tmp: {}".format(tmp))


print(a)

print(" ".join(ans))

